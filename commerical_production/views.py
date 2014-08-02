from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import Http404
from django.contrib import auth
from django.contrib.auth import views, login
from django import forms

from annoying.decorators import render_to, ajax_request

import commProd.models as cpm
from commProd.forms import RegForm

from helpers.view_helpers import get_rand_username, \
    render_err_msg, possesive, add_usr_to_query, \
    validate_email, get_floor_percentile, \
    get_day_trend, JSONResponse, render_to_response
from helpers.aws_put import put_profile_pic
from helpers.query_managers import commprod_query_manager, \
    profile_query_manager
from helpers.link_activator import get_active_page
from helpers.admin.utils import email_users
from helpers.admin import email_templates

from commerical_production.settings import ADMINS


def register(request, key):
    """
        Registration page. Visitor arrives wih activation key
    """
    profile = cpm.UserProfile.objects.filter(
        activation_key=key)

    if not profile.exists() or profile[0].user.is_active:
        hero_title = "Hmm... that registration key is invalid."
        return render_err_msg(request, hero_title)

    user = profile[0].user

    if request.POST:
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            user.is_active = True
            user.first_name = reg_form.cleaned_data['first_name']
            user.last_name = reg_form.cleaned_data['last_name']
            user.set_password(reg_form.cleaned_data['password'])

            pic_url = put_profile_pic(
                reg_form.cleaned_data['pic_url'], user.profile)
            if pic_url:
                user.profile.pic_url = pic_url

            user.profile.class_year = reg_form.cleaned_data['class_year']

            alt_emails = request.POST.getlist('alt_email')
            for alt_email in alt_emails:
                if alt_email:
                    user.profile.add_email(alt_email)

            user.save()
            user.profile.save()

            user = auth.authenticate(username=user.username,
                                     password=reg_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    # Redirect to a success page.
                    return redirect('/')

    else:
        reg_form = RegForm()

    template_values = {
        'page_title': "register",
        'form': reg_form,
        'user': user,
    }

    return render_to_response('register.html',
                              template_values, request)


def login(request, *args, **kwargs):
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return views.login(request, *args, **kwargs)


@login_required
def confirm_email(request, key):
    """
        Endpoint to confirm you are owner of email
    """
    alt_email = cpm.Email.objects.filter(activation_key=key)
    if alt_email.exists():
        alt_email[0].confirm()
        return redirect('/')
    hero_title = "We weren't able to complete your request..."
    return render_err_msg(request, hero_title)


@login_required
@ajax_request
def claim_email(request):
    """
        Endpoint to request an email be added to you profile
    """
    email = request.POST.get('email', "")
    email_user = User.objects.filter(email=email)
    payload = {
        'res': 'failed'
    }
    if email_user.exists() and \
            not email_user[0].profile.send_mail:
        request.user.profile.add_email(email)
        payload['res'] = 'success'

    return payload


@login_required
@ajax_request
def feedback(request):
    """
        Endpoint to request an email be added to you profile
    """
    feedback = request.POST.get('feedback', None)
    if not feedback:
        return {
            'res': 'failed'
        }
    feedback.replace('\n', '<br>')
    user = request.user
    subject = email_templates.feedback['subject']
    content = email_templates.feedback['content'] % \
        (user.username, feedback)
    admin_emails = [admin[1] for admin in ADMINS]
    email_users(subject, content, admin_emails,
                from_email=user.email)
    return {
        'res': 'success'
    }


@login_required
@render_to("welcome.html")
def welcome(request):
    """
        First page after successfully signing update
    """
    return dict(
        user=request.user
    )


@login_required
def home(request):
    """
        Landing page, top ten rated comm prods 
        and ten newest commprods
    """
    return redirect('commprod/')


@login_required
def profile(request, username):
    """
        User profile page,
        displays avg. overall score + list of commprods
        Profile can be gotten to by user_id, username, 
        or an alt_email
    """
    if User.objects.filter(username=username).exists():
        profile_user = User.objects.filter(
            username=username)[0]
    else:
        raise Http404

    page_username = get_rand_username(profile_user)

    request_type = request.GET.get('type', "")

    subnav_key, subnav_value, page_title = get_active_page(
        'profile', request_type)

    header = possesive(page_username, page_title)
    title = possesive(profile_user.username, page_title)

    template_values = {
        "page_title": title,
        'nav_profile': 'active',
        subnav_key: subnav_value,
        'header': header,
        'user': request.user,
        'profile_user': profile_user,
        'header-classes': '',
        'floor_percentile': get_floor_percentile(
            profile_user.profile),
        "trend": get_day_trend(profile_user.profile),
        "num_commprods": cpm.CommProd.objects.filter(
            user_profile=profile_user.profile).count(),
        "num_votes": cpm.Rating.objects.filter(
            user_profile=profile_user.profile).count()
    }

    if request_type != "":
        return profile_search(request,
                              template_values, profile_user)
    template_values.update(profile_query_manager(
        request.user, profile_user))
    return render_to_response('profile.html',
                              template_values, request)


def profile_search(request, template_values, profile_user):
    """
        Helper function to deal with recent/best 
        pages for user.
    """
    get_dict = add_usr_to_query(request.GET,
                                profile_user.username)
    template_values['commprod_timeline'] = commprod_query_manager(
        get_dict, user=request.user)
    template_values['header_classes'] = ''

    return render_to_response('profile_search.html',
                              template_values, request)


@login_required
def edit_profile(request):
    """
        Edit profile page
    """

    user = request.user
    profile = user.profile
    # update for post request

    if request.POST and request.is_ajax():
        success = False
        errors = {}
        request_type = request.POST.get('form_type', None)
        if request_type == "password":
            password = request.POST.get(
                'current_password', None)
            new_password = request.POST.get(
                'new_password', None)
            new_password_confirm = request.POST.get(
                'new_password_confirm', None)

            if user.check_password(password):
                if new_password is not None \
                        and new_password == new_password_confirm:
                    user.set_password(new_password)
                    success = 'Password changed'
                    user.save()
                else:
                    errors['password'] = ["Passwords don't match."]
            else:
                errors['password'] = ['Incorrect password.']

        elif request_type == "shirt_name":
            try:
                # delete all current shirt names
                cpm.ShirtName.objects.filter(
                    user_profile=profile,
                    editable=True).delete()

                # add in all new shirt names
                shirt_names = request.POST.getlist(
                    'shirt_name')
                for name in shirt_names:
                    name = name.strip()
                    if not name:
                        cpm.ShirtName(
                            user_profile=profile,
                            name=name).save()
                success = "Shirt names added!"
            except:
                errors['shirt_name'] = [
                    'Oops -- something went wrong.']

        elif request_type == "email":
            emails = request.POST.getlist('email')
            errors['email'] = []

            for email in emails:
                # makes sure email
                if not validate_email(email):
                    if not email.strip():
                        errors['email'].append(
                            "Empty email entered.")
                    else:
                        errors['email'].append(
                            '%s is not a valid email.' %
                            email)

                # make sure email doesn't exists
                elif cpm.UserProfile.objects.filter(
                        email__email=email,
                        email__confirmed=True).exists() \
                        or cpm.UserProfile.objects.filter(
                        user__email=email,
                        send_mail=True).exists():
                    errors['email'].append("""%s is already
                     re\gistered with an account.""" % email)

            if not errors['email']:
                for email in emails:
                    profile.add_email(email)
                success = "Confirmation emails sent out!"

        elif request_type == 'pic':
            pic_url = request.POST.get('pic_url')
            # download and upload to our S3
            pic_url = put_profile_pic(
                pic_url, user.profile)
            if pic_url:  # no errors/less than 1mb #patlsotw
                user.profile.pic_url = pic_url
                user.profile.save()
                success = "Profile picture changed!"
            else:
                errors['pic'] = [
                    'Oops -- something went wrong.']

        return_obj = {
            'success': success,
            'errors': errors
        }

        return JSONResponse(return_obj)

    # not post request
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
    for name in cpm.ShirtName.objects.filter(
            user_profile=profile).values_list('name', flat=True):
        field = {
            'name': 'shirt_name',
            'placeholder': 'Shirt name',
            'value': name
        }
        shirtNameForm.append(field)

    emailForm = [{'value': user.email}]
    for email in cpm.Email.objects.filter(
            user_profile=profile,
            confirmed=True).values_list('email', flat=True):
        field = {
            'value': email
        }
        emailForm.append(field)

    template_values = {
        "page_title": "Edit Profile",
        'nav_account': 'active',
        'user': request.user,
        'password': passwordForm,
        'shirtname': shirtNameForm,
        'email': emailForm
    }

    return render_to_response('edit_profile.html',
                              template_values, request)


def reset_password(request):
    errors = {'username': []}  # setup for javascript error setting
    success = False
    if request.POST:
        username = request.POST.get('username', None)
        if not username or not username.strip():
            errors['username'].append(
                "Empty username entered.")

            # make sure user exists
        elif not cpm.UserProfile.objects.filter(
                user__username=username,
                send_mail=True, user__is_active=True).exists():
            errors['username'].append(
                "%s is not registered with an account." %
                username)

            # create password reset object
        else:
            user_profile = cpm.UserProfile.objects.filter(
                user__username=username)[0]
            reset = cpm.PasswordReset(
                user_profile=user_profile, is_active=True)
            reset.save()
            reset.send_confirm_email()

        if not len(errors['username']):
            success = "Password reset email sent out!"

        return_obj = {
            'success': success,
            'errors': errors
        }

        return JSONResponse(return_obj)
    else:
        template_values = {
            'page_title': "Reset Password",
            "hero_err_title": "",
            'user': request.user,
        }

    return render_to_response('reset_password.html',
                              template_values, request)


@render_to("reset_password_confirm.html")
def reset_password_confirm(request, key=None):
    success = False
    errors = False
    if key:
        reset = cpm.PasswordReset.objects.filter(
            activation_key=key)
        if reset.exists() and reset[0].is_active and  \
                reset[0].is_valid():
            reset = reset[0]
            reset.is_active = False
            new_password = reset.get_new_passwd()
            reset.save()
            success = "Your password has been reset to %s " % new_password
        else:
            errors = "Your key is no longer active."
    else:
        errors = "Your key is invalid."

    if errors:
        errors += " <a href='/reset_password'> Try again </a>"
    return dict(
        page_title="Password Reset",
        user=request.user,
        success=success,
        errors=errors,
    )


@render_to("googlead6c3c617c310b08.html")
def google_verify(request):
    """
        page used to verify for chrome store
    """
    return {}
