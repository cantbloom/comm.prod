from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Sum

from helpers.renderers import donation_renderer

from donations.forms import AnonDonateForm, DonateForm
from donations.models import *

import stripe

from datetime import datetime
from os import environ as env
from itertools import chain
from operator import attrgetter


"""
Donation home page. Return all of the donation objects that are found.
"""
@login_required
def home(request):
    donations = Donation.objects.all()
    anon_donations = AnonDonation.objects.all()
    sorted_donations = sorted(list(chain(donations, anon_donations)), key=attrgetter('date'), reverse=True)
    page = request.GET.get('page', 1)
    rendered_donations = donation_renderer(sorted_donations, page)
    tot_donations = donations.count()
    sum_donations = 0
    if tot_donations != 0:
        sum_donations =  donations.aggregate(Sum('amount'))['amount__sum']
    template_values = {
        'page_title' : "Past Donations",
        'nav_donate' : "active",
        'donation_timeline' : rendered_donations,
        'tot_donations' : tot_donations,
        'sum_donations' : sum_donations,
    }

    return render_to_response('donations/home.html', template_values, context_instance=RequestContext(request))

"""
Donate page returns the form for submitting a donation
"""
def donate(request):

    template_values = {
        'page_title' : "Make a Donation",
        'nav_donate' : "active",
        'stripe_public_key' : env['STRIPE_PUBLIC_KEY']
    }

    if request.user.is_authenticated():
        return user_donate(request, template_values)

    return anon_donate(request, template_values)

"""
Method for dealing with donations from users with accounts. Saves the stripe customer id for later use.
"""
@login_required
def user_donate(request, template_values):
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            amount = form.cleaned_data['amount']
            is_anonymous = form.cleaned_data['is_anonymous']
            user_profile = request.user.profile

            description = 'Donation of $%s by %s on %s for %s' % (amount, user_profile.user.username, str(datetime.now()), reason)

            # set your secret key: remember to change this to your live secret key in production
            # see your keys here https://manage.stripe.com/account
            stripe.api_key = env["STRIPE_SECRET_KEY"]

            # get the credit card details submitted by the form
            token = request.POST['stripeToken']

            customer_id = user_profile.stripe_customer_id

            if customer_id == "no_id": #user did not save card in the past 

                # create a Customer
                customer = stripe.Customer.create(
                    card=token,
                    description=description
                )

                customer_id = customer.id

                # save the customer ID in your database so you can use it later
                user_profile.stripe_customer_id = customer_id
                user_profile.save()

            # charge the Customer
            stripe.Charge.create(
                amount=amount*100, # in cents
                currency="usd",
                customer=customer_id,
                description=description
            )
            
            #charge has gone through successfully
            donation = Donation(reason=reason, amount=amount, is_anonymous=is_anonymous, user_profile=user_profile)
            donation.save()

            return render_to_response('donations/donate_success.html', template_values, context_instance=RequestContext(request))

    else:
        form = DonateForm()

    template_values['form'] = form

    return render_to_response('donations/donate.html', template_values, context_instance=RequestContext(request))
"""
Method for dealing with donations from users without accounts. Does not save a stripe customer id and just charges the card directly.
"""
def anon_donate(request, template_values):
    if request.method == 'POST':
        form = AnonDonateForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            amount = form.cleaned_data['amount']

            description = 'AnonDonation of $%s on %s for %s' % (amount, str(datetime.now()), reason)

            # set your secret key: remember to change this to your live secret key in production
            # see your keys here https://manage.stripe.com/account
            stripe.api_key = env["STRIPE_SECRET_KEY"]

            # get the credit card details submitted by the form
            token = request.POST['stripeToken']

            # charge the Customer
            stripe.Charge.create(
                amount=amount*100, # in cents
                currency="usd",
                card=token,
                description=description
            )
            
            #charge has gone through successfully
            donation = AnonDonation(reason=reason, amount=amount)
            donation.save()

            return render_to_response('donations/donate_success.html', template_values, context_instance=RequestContext(request))

    else:
        form = AnonDonateForm()

    template_values['form'] = form

    return render_to_response('donations/donate.html', template_values, context_instance=RequestContext(request))