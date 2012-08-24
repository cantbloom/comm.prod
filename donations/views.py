from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Sum

from helpers.renderers import donation_renderer

from donations.forms import DonateForm
from donations.models import *

import stripe

from datetime import datetime
from os import environ as env

"""
Donation home page. Return all of the donation objects that are found.
"""
@login_required
def home(request):
    donations = Donation.objects.order_by('-date')
    page = request.GET.get('page', 1)
    rendered_donations = donation_renderer(donations, page)
    template_values = {
        'page_title' : "Past Donations",
        'nav_donate' : "active",
        'donation_timeline' : rendered_donations,
        'tot_donations' : donations.count(),
        'sum_donations' : donations.aggregate(Sum('amount'))['amount__sum']
    }

    return render_to_response('donations/home.html', template_values, context_instance=RequestContext(request))

"""
Donate page returns the form for submitting a donation
"""
@login_required
def donate(request):

    template_values = {
        'page_title' : "Make a Donation",
        'nav_donate' : "active",
        'stripe_public_key' : env['STRIPE_PUBLIC_KEY']
    }

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