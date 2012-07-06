from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth import authenticate, login, logout

from commProd.models import CommProd, Rating, UserProfile, ShirtName
from commProd.forms import RegForm

from helpers.view_helpers import getRandomUsername, renderErrorMessage, possesive
from helpers.aws_put import put_profile_pic
from helpers.query_managers import commprod_query_manager, profile_query_manager
from helpers.link_activator import get_active_page

"""
Registration page. Visitor arrives wih activation key
"""
@csrf_exempt
def register(request, key):
    #crf shit
    #c = {}
    #c.update(csrf(request))

    # #check if user is logged in
    # if not request.user.is_authenticated:
    #     page_title = "Oops"
    #     hero_title ="It seems you've already registered..." 
    #     return renderErrorMessage(request, page_title, hero_title)
    # #grab user profile, check if they are already registeded
    profile = UserProfile.objects.filter(activation_key=key)
    
    # ##switch BACK DONT FORGET
    # if not profile.exists() or not profile[0].user.is_active:
    #     page_title = "Oops"
    #     hero_title ="Hmm... that registration key is invalid."
    #     return renderErrorMessage(request, page_title, hero_title)

    user = profile[0].user

    if request.POST:
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            user.is_active = True
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.set_password(request.POST['password'])

            alt_email = request.POST['alt_email']
            pic_url = request.POST['pic_url']
            user.profile.mergeAndDelete(alt_email)
            user.profile.alt_email = alt_email
            user.profile.pic_url = put_profile_pic(pic_url) #download and upload to our S3
            
            ShirtName(user_profile=user.profile, name=request.POST['shirt_name']).save()
            
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
    }

    return render_to_response('register.html', template_values, context_instance=RequestContext(request))

"""
Landing page, top ten rated comm prods + ten newest commprods 
"""
@login_required
def home(request):
    subnav_key, subnav_value, title =  get_active_page('home', request.GET.get('type', ""))

    template_values = {
        'page_title' : "Home",
        'nav_home' : "active",
        subnav_key : subnav_value,
    }
    return render_to_response('home.html', template_values, context_instance=RequestContext(request))

"""
User profile page, 
displays avg. overall score + list of commprods
Profile can be gotten to by user_id, username, or an alt_email
"""
@login_required
def profile(request, username=None):
    if username and User.objects.filter(username=username).exists():
        user = User.objects.filter(username=username)[0]
    else:
        raise Http404

    page_username = getRandomUsername(user)

    subnav_key, subnav_value, title =  get_active_page('profile', request.GET.get('type', ""))
    
    title = possesive(user.username, title)
    
    template_values = {
        "page_title": title,
        'nav_profile' : 'active',
        subnav_key : subnav_value,
        'header' : title,
    }
    
    if request.GET != {}:
        return profile_search(request, template_values, username)
    else:
        template_values.update(profile_query_manager(user))
        return render_to_response('profile.html', 
        template_values, context_instance=RequestContext(request))

"""Helper function to deal with recent/popular
search queries
"""
def profile_search(request, template_values, username):
    template_values['commprod_timeline'] = commprod_query_manager(request.GET, username=username)

    return render_to_response('profile_search.html', 
        template_values, context_instance=RequestContext(request))