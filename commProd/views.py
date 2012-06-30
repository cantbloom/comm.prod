from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from commProd.models import CommProd, Rating, UserProfile
from commProd.forms import RegForm
from commerical_production.config import KEY
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import Http404
import re
import datetime
import random


"""
Registration page. Visitor arrives wih activation key
"""
@csrf_exempt
def register(request, key):
    #crf shit
    #c = {}
    #c.update(csrf(request))

    ##switch BACK DONT FORGET
    if not request.user.is_authenticated:
        return redirect("/")
    #check if key is valid and unregistered
    profile = UserProfile.objects.filter(activation_key=key)
    ##switch BACK DONT FORGET
    if not profile.exists() or profile[0].user.is_active:
        return redirect('/invalid_reg')

    user = profile[0].user

    if request.POST:
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.set_password(request.POST['password'])
            user.profile.alt_email = request.POST['alt_email']
            user.profile.shirt_names = request.POST['shirt_name']
            user.is_active = True
            user.save()
            user.profile.save()
            
            return HttpResponse('valid', mimetype='text/plain')
        
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
Helpful message for the retards
"""
def invalid_reg(request):
    if request.user.is_authenticated:
        return redirect("/")

    template_values = {
        'page_title': "Oops",
        'user_profile' : "/",
    }

    return render_to_response('invalid_reg.html', 
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
    
    commprods = CommProd.objects.filter(author=user.id)


    page_username = getUsername(user)
    template_values = {
        "page_title": user.username +"'s Profile",
        'user_profile' : "/users/" + request.user.username,
        'commprods' : commprods,
        'username' : page_username

    }
    return render_to_response('profile.html', 
        template_values, context_instance=RequestContext(request))



@login_required
def search(request):

    template_values = {

        "page_title": request.users.username +"'s Profile",
        'user_profile' : "/users/" + request.user.username,

    }
    return render_to_response('nothing.html',
     template_values, context_instance=RequestContext(request))




###### request endpoints #######
@login_required
def vote (request):
    vote = request.POST["vote"]
    cp_id = request.POST["id"]
    user_id = requset.user.id
    valid_votes = [0, 0.5, 1, 1.5, 2, 2.5, 3]
    comm_prod = CommProd.objects.filter(cp_id__exact=cp_id)
    rating = Rating.objects.filter(cp_id__exact=cp_id, user_id__exact=user_id)
    avg = None
    if vote_val in valid_votes and comm_prod.exists():
        if rating.exists():
            rating.update(vote=vote, date=datetime.datetime.now())
        else:
            rating = Rating(cp_id=cp_id, user_id=user_id, vote=vote)
        avg = getAvg(cp_id)        

        success = True
    else:
        success = False
    
    payload = {"success": success, "cp_id": 
        cp_id, "vote": vote, "avg": avg}
    data = json.dumps(payload)
    return HttpResponse(data, mimetype='application/json') 


@csrf_exempt
def processMail(request):
    data = request.POST.get("data", None)
    key = request.POST.get("key", None)
    resp = ""
    if data and str(key) == KEY:
        data = json.loads(data) #[{sender : (content, comm_prods)}]
        for dic in data:
            sender = dic.keys()[0]
            content = dic[sender][0]
            comm_prods = dic[sender][1]
            user_id = None
            email_search = User.objects.filter(email__exact=sender)
            alt_email_search = UserProfile.objects.filter(alt_email__exact=sender)

            if email_search.exists():
                user_id = email_search[0].id
            elif alt_email_search.exists():
                user_id = alt_email_search[0].user.id
            else:
                resp += "\nUser %s not found\n" % sender
            
            if user_id:
                resp += "\nUser %s found with comm prods:\n %s" % (sender, comm_prods)
                for prod in comm_prods:
                    cp = CommProd(content=content, comm_prod=prod, author=user_id)
                    cp.save() 
    else:
        resp = "No data"
        if str(key) != KEY:
            resp = "Success!"
    return HttpResponse(resp, mimetype="text/plain")

#########HELPERS###################

"""
Returns a username to be rendered choosing randomly between
first + last, username, and a shirt first_name.
"""
def getUsername(user):
    potentials = json.loads(user.shirt_names)
    potentials.append(user.first_name + user.last_name)
    potentials.append(user.username)
    return random.choice(potentials)

"""
Gets the avg rating of the commprod.
Updates the CommProd object to reflect the
latest average. cp_id is assumed to be
a valid id (object exists)
"""
def getAvg(cp_id):
    rating_query =  Rating.objects.filter(cp_id__exact=cp_id)
    total = sum(row.vote for row in rating_query)
    if len(rating_query) != 0:
        avg = float(total/len(rating_query))
    else:
        avg = 0

    prod = CommProd.objects.filter(cp_id=cp_id)[0]
    prod.update(score=avg)
    prod.save()
    return avg
"""
Returns a tuple of (user, prod, date)
With the username given and the date formatted
as mm-dd
"""
def getCommProd(cp_id):
    pass

