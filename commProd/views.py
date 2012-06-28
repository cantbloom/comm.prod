from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from commProd.models import CommProd, Rating, UserProfile
import re
from django.shortcuts import redirect
import datetime

"""
Landing page, top ten rated comm prods + ten newest commprods 
"""
@login_required
def home(request):

    ##TODO
    template_values = {

    }
    return render_to_response('home.html', template_values)

"""
Registration page. Visitor arrives wih activation key
"""
def register(request, key):
    #check if key is valid and unregistered
    try:
        profile = UserProfile.objects.get(activation_key=key)
        user = profile.user
        if user.is_active:
            return redirect('/')

    except:
        return redirect('/')


    template_values = {
        'key': key,
        'email' : user.email
    }
    return render_to_response('register.html', template_values)



"""
User profile page, 
displays avg. overall score + list of commprods
"""
@login_required
def user(request):
    ##TODO

    template_values = {

    }
    return render_to_response('commProd/user.html', template_values)

@login_required
def search(request):
    data  = 'a'
    data = json.dumps(data)

    return HttpResponse(data, mimetype='application/json')




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


def processMail(request):
    data = request.POST["data"]
    resp = ""
    if data:
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
                resp += "User %s not found\n" % sender
            
            if user_id:
                for prod in comm_prods:
                    cp = CommProd(content=content, comm_prod=prod, author=user_id)
                    cp.save() 
    else:
        resp = "No data"
    return HttpResponse(resp, mimetype="text/plain")

def getAvg(cp_id):
    rating_query =  Rating.objects.filter(cp_id__exact=cp_id))
    total = sum(row.vote for row in rating_query)
    return total/len(rating_query)

