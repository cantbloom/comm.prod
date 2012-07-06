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

from commProd.models import CommProd, Rating, UserProfile
from commerical_production import config

from helpers.view_helpers import getRandomUsername, renderErrorMessage
from helpers.commprod_search import commprod_search
from helpers.admin.utils import createUser
from helpers.aws_put import put_profile_pic
from helpers.query_managers import commprod_query_manager

import  time


@login_required
def search(request):

    template_values = {
        "user": request.user,
        'commprod_timeline' : commprod_queryManager(request.GET)

    }
    return render_to_response('search.html', template_values, context_instance=RequestContext(request))

###### request endpoints #######
@login_required
@csrf_exempt
def vote (request):
    valid_votes = ['-1','1'] #patlsotw 

    score = request.POST["score"]
    cp_id = request.POST["id"]
    user = request.user

    commprod = commprod_search(cp_id=cp_id)[0]

    if not commprod:
        return HttpResponse(json.dumps({'success':False}), mimetype='application/json')

    rating, created = Rating.objects.get_or_create(commprod=commprod, user_profile=user.profile)

    if score in valid_votes:
        rating.previous_score = rating.score
        rating.score = score
        rating.save() #updates commprod avg automatically with postsave signal
    
    payload = {
        "success": True,
        "cp_id": cp_id,
        "rating": float(score),
        "cp_score": commprod.score
    }

    return_data = json.dumps(payload)

    return HttpResponse(return_data, mimetype='application/json') 

@login_required
@csrf_exempt
def api_search (request):
   return HttpResponse(commprod_query_manager(request.GET))

@csrf_exempt
def processProd(request):
    data = request.POST.get("data", None)
    key = request.POST.get("key", None)
    
    resp = ""
    if data and str(key) == config.SECRET_KEY:
        data = json.loads(data) #{sender : (content, [comm_prods], date)}
        sender = data.keys()[0]
        content, commprods, date = data[sender]

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
            commprod, created = CommProd.objects.get_or_create(email_content=content, commprod_content=commprod, user_profile=user.profile, date=date) 
            if created:
                commprod.save()
            resp += "Added?" + str(created)
    else:
        resp = "No data"
        if str(key) != config.SECRET_KEY: #patlsotw
            resp = "Success!"
    return HttpResponse(resp, mimetype="text/plain")




