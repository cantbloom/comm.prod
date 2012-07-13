from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django import forms

from commProd.models import CommProd, Rating, UserProfile, ShirtName, Email
from commProd.forms import RegForm

from helpers.view_helpers import getRandomUsername, renderErrorMessage, possesive, addUserToQuery, validateEmail
from helpers.aws_put import put_profile_pic
from helpers.query_managers import commprod_query_manager, profile_query_manager
from helpers.link_activator import get_active_page
from helpers.admin.utils import emailUsers
from helpers.admin import email_templates

from commerical_production.settings import ADMINS

import json

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

            pic_url = request.POST['pic_url']
            user.profile.pic_url = pic_url

            ShirtName(user_profile=user.profile, name=request.POST['shirt_name']).save()

            alt_emails = request.POST.getlist('alt_email')
            for alt_email in alt_emails:
                if alt_email != "":
                    user.profile.add_email(alt_email)
            
            user.save()
            user.profile.save()
            
            user = authenticate(username=user.username, password=request.POST['password'])
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

def login(request, *args, **kwargs):
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return auth_views.login(request, *args, **kwargs)

"""
Endpoint to confirm you are owner of email
"""
@login_required
@csrf_exempt
def confirm_email(request, key):
    alt_email = Email.objects.filter(activation_key=key)
    if alt_email.exists():
        alt_email[0].confirm()
        return redirect('/')

    return redirect('/invalid_reg')

"""
Endpoint to request an email be added to you profile
"""
@login_required
@csrf_exempt
def claim_email(request):
    email = request.POST.get('email', "")
    email_user = User.objects.filter(email = email)
    if email_user.exists() and email_user[0].profile.send_mail == False:
        request.user.profile.add_email(email)
        return HttpResponse(json.dumps({'res':'success'}), mimetype='application/json') 
    return HttpResponse(json.dumps({'res':'failed'}), mimetype='application/json') 

"""
Endpoint to request an email be added to you profile
"""
@login_required
@csrf_exempt
def feedback(request):
    feedback = request.POST.get('feedback', None)
    if not feedback:
        return HttpResponse(json.dumps({'res':'failed'}), mimetype='application/json') 
    feedback.replace('\n', '<br>')
    user = request.user
    subject = email_templates.feedback['subject']
    content = email_templates.feedback['content'] % (user.username, feedback)
    admin_emails = [admin[1] for admin in ADMINS]
    emailUsers(subject, content, admin_emails)
    return HttpResponse(json.dumps({'res':'success'}), mimetype='application/json') 

"""
First page after successfully signing update
"""
@login_required
def welcome(request):
    template_values = {
        'user': request.user
    }

    return render_to_response('welcome.html', template_values, context_instance=RequestContext(request))


"""
Landing page, top ten rated comm prods + ten newest commprods 
"""
@login_required
def home(request):
    return redirect('commprod/')

"""
User profile page, 
displays avg. overall score + list of commprods
Profile can be gotten to by user_id, username, or an alt_email
"""
@login_required
def profile(request, username):
    if User.objects.filter(username=username).exists():
        profile_user = User.objects.filter(username=username)[0]
    else:
        raise Http404

    page_username = getRandomUsername(profile_user)

    request_type = request.GET.get('type', "")

    subnav_key, subnav_value, page_title =  get_active_page('profile', request_type)

    header = possesive(page_username, page_title)
    title = possesive(profile_user.username, page_title)
    template_values = {
        "page_title": title ,
        'nav_profile' : 'active',
        subnav_key : subnav_value,
        'header' : header,
        'user'  : request.user,
        'profile_user' : profile_user,
    }
    
    if request_type != "":
        return profile_search(request, template_values, profile_user)
    else:
        template_values.update(profile_query_manager(profile_user))
        return render_to_response('profile.html', 
        template_values, context_instance=RequestContext(request))
"""
Edit profile page
"""
@login_required
@csrf_exempt
def edit_profile(request):
    user = request.user
    profile = user.profile
    ##update for post request

    if request.POST and request.is_ajax():
        success = False
        errors = {}
        type = request.POST.get('form_type', None)
        if type == "password":
            password = request.POST.get('current_password', None)
            new_password = request.POST.get('new_password', None)
            new_password_confirm = request.POST.get('new_password_confirm', None)

            if user.check_password(password):
                if new_password!=None and new_password == new_password_confirm:
                    user.set_password(new_password)
                    success = 'Password changed'
                else:
                    errors['password'] = ["Passwords don't match."]
            else:
                errors['password'] = ['Incorrect password.']
        
        elif type == "shirt_name":
            try:
                #delete all current shirt names
                ShirtName.objects.filter(user_profile=profile, editable = True).delete()

                #add in all new shirt names
                shirt_names = request.POST.getlist('shirt_name')
                for name in shirt_names:
                    name = name.strip()
                    if name != "":
                        ShirtName(user_profile=profile, name=name).save()

                success = 'Shirt names added!'

            except:
                errors['shirt_name'] = ['Oops -- something went wrong.']

        elif type == "email":
            emails = request.POST.getlist('email')
            errors['email'] = []

            for email in emails:
                #makes sure email
                if not validateEmail(email): 
                    errors['email'].append(email + ' is not a valid email.')

                #make sure email doesn't exists
                elif UserProfile.objects.filter(email__email=email, email__confirmed=True).exists() or UserProfile.objects.filter(user__email=email, send_mail=True).exists():
                    errors['email'].append(email + ' is already registered with an account.')

            if errors['email'] == []:
                for email in emails:
                    profile.add_email(email)
                success = "Confirmation emails sent out!"

        elif type == 'pic':
            pic_url = request.POST.get('pic_url')
            pic_url = put_profile_pic(pic_url, user.profile) #download and upload to our S3
            if pic_url: #no errors/less than 1mb #patlsotw
                user.profile.pic_url = pic_url
                success = "Profile picture changed!"
            else:
                errors['pic'] = ['Oops -- something went wrong.']

        return_obj = {
            'success' : success,
            'errors': errors
        }

        return HttpResponse(json.dumps(return_obj), mimetype='application/json') 

    #not post request
    passwordForm = [
        {
            'name': 'current_password',
            'placeholder': 'Current password'
        },
        {
            'name': 'new_password',
            'placeholder': 'New password'
        },
        {
            'name': 'new_password_confirm',
            'placeholder': 'Confirm new password'
        }
    ]

    shirtNameForm = []
    for name in ShirtName.objects.filter(user_profile = profile).values_list('name', flat=True):
        field = {
            'name': 'shirt_name',
            'placeholder': 'Shirt name',
            'value': name
        }
        shirtNameForm.append(field)

    emailForm = [{'value':user.email}]
    for email in Email.objects.filter(user_profile = profile, confirmed=True).values_list('email', flat=True):
        field = {
            'value': email
        }
        emailForm.append(field)


    template_values = {
        "page_title": "Edit Profile",
        'user'  : request.user,
        'password': passwordForm,
        'shirtname': shirtNameForm,
        'email': emailForm

    }
    
    return render_to_response('edit_profile.html', template_values, context_instance=RequestContext(request))
"""
Helper function to deal with recent/popular
search queries
"""
def profile_search(request, template_values, profile_user):
    get_dict = addUserToQuery(request.GET, profile_user.username)
    template_values['commprod_timeline'] = commprod_query_manager(get_dict, user=profile_user)

    return render_to_response('profile_search.html', 
        template_values, context_instance=RequestContext(request))
