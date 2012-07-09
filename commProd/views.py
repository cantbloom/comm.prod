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

from commProd.models import CommProd, Rating, UserProfile, Correction
from commerical_production import config

from helpers.view_helpers import getRandomUsername, renderErrorMessage
from helpers.commprod_search import commprod_search
from helpers.admin.utils import createUser
from helpers.aws_put import put_profile_pic
from helpers.query_managers import commprod_query_manager, vs_data_manager, trend_data_manager, correction_query_manager
from helpers.link_activator import get_active_page
from helpers.renderers import commprod_renderer

from django.utils.safestring import mark_safe



"""
Landing page, top ten rated comm prods + ten newest commprods 
"""
@login_required
def home(request):
    template_values = {
        'page_title' : "CommProd Home",
        'nav_commprod' : "active",
        'subnav_home' : "active",
        #'trending_time#line': commprod_query_manager({'type':'trending', 'limit':10, 'page':1}, request.user),
        'unvoted_commprods': mark_safe(str(commprod_query_manager({'unvoted':True, 'limit':30}, request.user, 'list'))),
        'user_profile':request.user.profile
    }

    return render_to_response('commprod/home.html', template_values, context_instance=RequestContext(request))

@login_required
def search(request):
    subnav_key, subnav_value, title =  get_active_page('home', request.GET.get('type', ""))
    template_values = {
        'page_title' : subnav_key.split("_")[1].capitalize() + " CommProds",
        'user': request.user,
        'commprod_timeline' : commprod_query_manager(request.GET, request.user),
        subnav_key : subnav_value,
    }
    return render_to_response('commprod/search.html', template_values, context_instance=RequestContext(request))

@login_required
def permalink(request, username, cp_id):
    get_dict = {'username' : username, 'cp_id' : cp_id}
    
    commprod = commprod_query_manager(get_dict, request.user, 'list')
    if len(commprod) == 1:
        rendered_commprod = commprod[0]
        cp_user = User.objects.filter(username=username)[0]
        commprod = CommProd.objects.filter(id=cp_id)[0]
        corrections = Correction.objects.filter(commprod=commprod)
    
    else:
        raise Http404

    template_values = {
        'user': request.user,
        'page_title' : "CommProd Permalink",
        'rendered_commprod' : rendered_commprod,
        'commprod' : commprod,
        'corrections' : corrections
    }
    return render_to_response('commprod/permalink.html', template_values, context_instance=RequestContext(request))

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
    return_type =  request.GET.get("return_type", 'html')
    res = { 'res':commprod_query_manager(request.GET, request.user, return_type)}
    return HttpResponse(json.dumps(res), mimetype='application/json')

@login_required
def profile_data(request):
    response_data = None #patlsotw
    
    type = request.GET.get('type', None)
    filter = request.GET.get('filter', None)
    username = request.GET.get('username', None)
    if username and User.objects.filter(username=username).exists():
        user = User.objects.filter(username=username)[0]
        
        if type == "trend":
            response_data = trend_data_manager(user)
        elif type == "vs_data":
            response_data = vs_data_manager(user, filter)
    
    return HttpResponse(json.dumps(response_data), mimetype="application/json")

@login_required
@csrf_exempt
def correction(request):
    user = request.user
    cp_id = request.POST.get('cp_id', None)
    content = request.POST.get('content', None)
    if (cp_id and content) and CommProd.objects.filter(id=cp_id).exists():
        commprod = CommProd.objects.filter(id=cp_id)[0]
        correction = Correction(user_profile=user.profile, commprod_content=content, commprod=commprod)
        correction.save()
        response_data = {
            'correction' : correction_query_manager(correction.id)
        }
    else:
        response_data = {
        'nodata' : ''
        }

    return HttpResponse(json.dumps(response_data), mimetype="application/json") 

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
            resp += "\nAdded?" + str(created)
    else:
        resp = "No data"
        if str(key) != config.SECRET_KEY: #patlsotw
            resp = "Success!"
    return HttpResponse(resp, mimetype="text/plain")




