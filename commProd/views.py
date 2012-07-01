from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth import authenticate, login

from commProd.models import CommProd, Rating, UserProfile, ShirtName
from commProd.forms import RegForm
from commerical_production import config

from helpers.view_helpers import getRandomUsername, renderErrorMessage
from helpers.commprod_search import commprod_search
from helpers.admin.utils import createUser

"""
Registration page. Visitor arrives wih activation key
"""
@csrf_exempt
def register(request, key):
    #crf shit
    #c = {}
    #c.update(csrf(request))

    #check if user is logged in
    if request.user.is_authenticated:
        page_title = "Oops"
        hero_title ="It seems you've already registered..." 
        return renderErrorMessage(request, page_title, hero_title)
    #grab user profile, check if they are already registeded
    profile = UserProfile.objects.filter(activation_key=key)
    
    ##switch BACK DONT FORGET
    if not profile.exists() or not profile[0].user.is_active:
        page_title = "Oops"
        hero_title ="Hmm... that registration key is invalid."
        return renderErrorMessage(request, page_title, hero_title)

    user = profile[0].user

    if request.POST:
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            user.is_active = True
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.set_password(request.POST['password'])

            alt_email = request.POST['alt_email']
            user.profile.mergeAndDelete(alt_email)
            user.profile.alt_email = alt_email
            
            ShirtName(user=user, name=request.POST['shirt_name']).save()
            
            user.save()
            user.profile.save()
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('/')

            return redirect('/invalid_reg')
        
    else:
        reg_form = RegForm()

    template_values = {
        'page_title': "Registration",
        'form' : reg_form,
        'user' : user,
        'user_profile' : "/users/" + request.user.username,
    }

    return render_to_response('register.html', 
        template_values, context_instance=RequestContext(request))

"""
Landing page, top ten rated comm prods + ten newest commprods 
"""
@login_required
def home(request):

    
    template_values = {
        'page_title' : "Home",
        'user_profile' : "/users/" + request.user.username,
    }
    return render_to_response('home.html', 
        template_values, context_instance=RequestContext(request))


"""
User profile page, 
displays avg. overall score + list of commprods
"""
@login_required
def profile(request, user_id=None, username=None):
    if user_id and User.objects.filter(id=user_id).exists():
        user = User.objects.filter(id=user_id)[0]
    elif username and User.objects.filter(username=username).exists():
        user = User.objects.filter(username=username)[0]
    else:
        raise Http404
    
    commprods = CommProd.objects.filter(user=user)


    page_username = getRandomUsername(user)
    template_values = {
        "page_title": user.username +"'s Profile",
        'user_profile' : "/users/" + request.user.username,
        'commprods' : commprods,
        'user_name' : page_username

    }
    return render_to_response('profile.html', 
        template_values, context_instance=RequestContext(request))



@login_required
def search(request, title, **kwargs):
    template_values = {
        "page_title": title,
        "user": request.user,
        'commprods' : commprod_search(**kwargs)
    }

    return render_to_response('search.html', template_values, context_instance=RequestContext(request))




###### request endpoints #######
@login_required
def vote (request):
    valid_votes = [0, 0.5, 1, 1.5, 2, 2.5, 3] #patlsotw 

    score = request.POST["score"]
    cp_id = request.POST["id"]
    user = requset.user

    commprod = commprod_search(id=cp_id)

    if not commprod:
        return HttpResponse(json.dumps({'success':False}), mimetype='application/json')

    rating = Rating.objects.get_or_create(commprod=commprod, user=user)

    if vote_val in valid_votes:
        rating.score = score
        rating.save() #updates commprod avg automatically with postsave signal
    
    payload = {
        "success": True,
        "cp_id": cp_id,
        "score": score,
        "avg": commprod.avg_score
    }

    return_data = json.dumps(payload)

    return HttpResponse(return_data, mimetype='application/json') 


@csrf_exempt
def processProd(request):
    data = request.POST.get("data", None)
    key = request.POST.get("key", None)
    
    resp = ""
    if data and str(key) == config.SECRET_KEY:
        data = json.loads(data) #[{sender : (content, [comm_prods])}]
        for dic in data:
            sender = dic.keys()[0]
            content, commprods = dic[sender]

            user = None
            email_search = User.objects.filter(email=sender)
            alt_email_search = UserProfile.objects.filter(alt_email=sender)

            if email_search.exists():
                user = email_search[0]
            elif alt_email_search.exists():
                user = alt_email_search[0].user
            else:
                user, created = createUser(sender, sender)
            
            resp += "\nUser %s with comm prods:\n %s" % (sender, commprods)
            
            for commprod in commprods:
                CommProd(email_content=content, commprod_content=commprod, user=user).save() 
    else:
        resp = "No data"
        if str(key) != config.SECRET_KEY: #patlsotw
            resp = "Success!"
    return HttpResponse(resp, mimetype="text/plain")




