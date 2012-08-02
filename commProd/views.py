from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth import authenticate, login

from commProd.models import CommProd, Rating, UserProfile, Correction, CorrectionRating, CommProdEmail

from helpers.view_helpers import getRandomUsername, renderErrorMessage, vote_commprod, vote_correction
from helpers.commprod_search import commprod_search
from helpers.admin.utils import createUser
from helpers.aws_put import put_profile_pic
from helpers.query_managers import commprod_query_manager, vs_data_manager, trend_data_manager, correction_query_manager
from helpers.link_activator import get_active_page
from helpers.renderers import commprod_renderer
from helpers.urlize_email_content import urlize_email_content

from os import environ as env


"""
Landing page, top ten rated comm prods + ten newest commprods
"""
@login_required
def home(request):
    template_values = {
        'page_title' : "Vote on these comm.prods we think you'll like",
        'nav_commprod' : "active",
        'subnav_home' : "active",
        'unvoted_commprods': str(commprod_query_manager({'unvoted':True, 'orderBy': '?', 'limit':30}, request.user, 'list')),
        'user_profile':request.user.profile
    }

    return render_to_response('commprod/home.html', template_values, context_instance=RequestContext(request))

@login_required
def search(request):
    subnav_key, subnav_value, title =  get_active_page('home', request.GET.get('type', ""))
    template_values = {
        'page_title' : subnav_key.split("_")[1],
        'nav_commprod' : "active",
        'user': request.user,
        'commprod_timeline' : commprod_query_manager(request.GET, request.user),
        subnav_key : subnav_value
    }
    return render_to_response('commprod/search.html', template_values, context_instance=RequestContext(request))

@login_required
def permalink(request, username, cp_id):
    get_dict = {'username' : username, 'cp_id' : cp_id}

    commprod = commprod_query_manager(get_dict, request.user, return_type='list')
    if len(commprod) == 1:
        rendered_commprod = commprod[0]
        cp_user = User.objects.filter(username=username)[0]
        commprod = CommProd.objects.filter(id=cp_id)[0]
        corrections = correction_query_manager(user=request.user, commprod=commprod)

        commprods = CommProd.objects.filter(email_content=commprod.email_content)
        email_content = urlize_email_content(commprod.email_content.content, commprods)
    else:
        raise Http404

    template_values = {
        'user': request.user,
        'page_title' : "permalink",
        'nav_commprod' : "active",
        'rendered_commprod' : rendered_commprod,
        'commprod' : commprod,
        'corrections' : corrections,
        'email_content' : email_content,
    }
    return render_to_response('commprod/permalink.html', template_values, context_instance=RequestContext(request))


"""
Frontend endpoint for adding commprods that are not picked up by the parser
"""
@staff_member_required
def admin(request):
    template_values = {
        'key' : env['SECRET_KEY']
    }
    return render_to_response('commprod/admin.html', template_values, context_instance=RequestContext(request))

###### request endpoints #######
@login_required
@csrf_exempt
def vote (request):
    types = ['commprod' , 'correction']
    valid_votes = ['-1','1'] #patlsotw
    payload = {'success' : False}

    score = request.POST.get("score", None)
    id = request.POST.get("id", None)
    type = request.POST.get("type", None)
    user = request.user


    if type in types and score and id:
        if type == "commprod":
            rating, obj = vote_commprod(id, score, user)
        elif type == "correction":
            rating, obj = vote_correction(id, score, user)

        if rating and score in valid_votes:
            rating.score = score
            rating.save() #updates object avg automatically during save

            payload = {
                "success": True,
                "id": id,
                "rating": float(score),
                "score": obj.score,
                "type": type
            }

    return_data = json.dumps(payload)

    return HttpResponse(return_data, mimetype='application/json')

@login_required
@csrf_exempt
def api_search (request):
    return_type = request.GET.get("return_type", 'html')
    res = {'res' : commprod_query_manager(request.GET, request.user, return_type)}
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
        correction = Correction(user_profile=user.profile, content=content, commprod=commprod)
        correction.save()
        response_data = {
            'correction' : correction_query_manager(user=request.user, correction_id=correction.id)
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
    print data
    print key
    resp = ""
    if data and str(key) == env['SECRET_KEY']:
        data = json.loads(data) #{sender : (content, [comm_prods], date, subject)}
        sender = data.keys()[0]
        content, commprods, date, subject = data[sender]

        user = None
        email_search = User.objects.filter(email=sender)
        alt_email_search = UserProfile.objects.filter(email__email=sender, email__confirmed=True)

        if email_search.exists():
            user = email_search[0]
        elif alt_email_search.exists():
            user = alt_email_search[0].user
        else:
            user, created = createUser(sender, sender)

        resp += "\nUser %s with comm prods:\n %s" % (sender, commprods)

        for commprod in commprods:
            email_content, created = CommProdEmail.objects.get_or_create(user_profile=user.profile, content=content, subject=subject, date=date)
            if created:
                email_content.save()

            commprod, created = CommProd.objects.get_or_create(email_content=email_content, content=commprod, original_content=commprod, user_profile=user.profile, date=date)
            if created:
                commprod.save()
            resp += "\nAdded? " + str(created)
    else:
        resp = "No data"
        if str(key) != env['SECRET_KEY']: #patlsotw
            resp = "Success!"
    return HttpResponse(resp, mimetype="text/plain")
