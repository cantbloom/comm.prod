from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from annoying.decorators import render_to

from helpers.renderers import donation_renderer
from helpers.view_helpers import _get_donation_stats, \
    render_to_response

from donations.forms import AnonDonateForm, DonateForm
import donations.models as dm

from datetime import datetime
from os import environ as env
from itertools import chain
from operator import attrgetter

import stripe


@login_required
@render_to("donations/home.html")
def home(request):
    """
        Donation home page. Return all of the 
        donation objects that are found.
    """

    donations = dm.Donation.objects.all()
    anon_donations = dm.AnonDonation.objects.all()

    sorted_donations = sorted(list(chain(donations,
                                         anon_donations)),
                              key=attrgetter('date'), reverse=True)
    page = request.GET.get('page', 1)
    rendered_donations = donation_renderer(
        sorted_donations, page)

    template_values = {
        'page_title': "Past Donations",
        'nav_donate': "active",
        'donation_timeline': rendered_donations,
    }

    template_values.update(_get_donation_stats(
        donations, anon_donations))

    return template_values


def donate(request):
    """
        Donate page returns the form for submitting a donation
    """

    template_values = {
        'page_title': "Make a Donation",
        'nav_donate': "active",
        'stripe_public_key': env['STRIPE_PUBLIC_KEY'],
    }

    template_values.update(_get_donation_stats())

    if request.user.is_authenticated():
        return user_donate(request, template_values)

    return anon_donate(request, template_values)


@login_required
def user_donate(request, template_values):
    """
    Method for dealing with donations from users with accounts. Saves the stripe customer id for later use.
    """
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            amount = form.cleaned_data['amount']
            is_anonymous = form.cleaned_data['is_anonymous']
            user_profile = request.user.profile

            description = """Donation of $%(amount)s.00 
            by %(username)s on %(date)s 
            for %(reason)s""" % {
                'amount': amount,
                'username':  user_profile.user.username,
                'date': datetime.now(),
                'reason':  reason
            }

            # set your secret key: remember to
            # change this to your live secret key in production
            # see your keys here
            # https://manage.stripe.com/account
            stripe.api_key = env["STRIPE_SECRET_KEY"]

            # get the credit card details
            # submitted by the form
            token = request.POST.get('stripeToken', '')

            if not token:
                return redirect('/donate')

            # customer_id = user_profile.stripe_customer_id

            # user did not save card in the past
            # if customer_id == "no_id":

            # create a Customer
            #     customer = stripe.Customer.create(
            #         card=token,
            #         description=description
            #     )

            #     customer_id = customer.id

            # save the customer ID in your
            #      database so you can use it later
            #     user_profile.stripe_customer_id = customer_id
            #     user_profile.save()

            # charge the Customer
            stripe.Charge.create(
                amount=amount * 100,  # in cents
                currency="usd",
                card=token,
                description=description
            )

            # charge has gone through successfully
            donation = dm.Donation(reason=reason,
                                   amount=amount,
                                   is_anonymous=is_anonymous,
                                   user_profile=user_profile)
            donation.save()

            template_values = {
                "amount": amount,
                "reason": reason,
            }

            return render_to_response(
                'donations/donate_success.html',
                template_values, request)

    else:
        form = DonateForm()

    template_values.update({
        'form': form,
    })

    return render_to_response(
        'donations/donate.html', template_values, request)


def anon_donate(request, template_values):
    """
        Method for dealing with donations
         from users without accounts. 
         Does not save a stripe customer id 
         and just charges the card directly.
    """
    if request.method == 'POST':
        form = AnonDonateForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            amount = form.cleaned_data['amount']
            name = form.cleaned_data['name']

            description = """AnonDonation by %(name)s of 
                $%(amount)s.00 on %(date)s for %(reason)s""" % {
                'name': name,
                'amount':  amount,
                'date': datetime.now(),
                'reason':  reason,
            }

            # set your secret key: remember to
            # change this to your live secret key in production
            # see your keys here
            # https://manage.stripe.com/account
            stripe.api_key = env["STRIPE_SECRET_KEY"]

            # get the credit card details submitted
            # by the form
            token = request.POST['stripeToken']

            # charge the Customer
            stripe.Charge.create(
                amount=amount * 100,  # in cents
                currency="usd",
                card=token,
                description=description
            )

            # charge has gone through successfully
            donation = dm.AnonDonation(name=name,
                                       reason=reason, amount=amount)
            donation.save()

            template_values = {
                "amount": amount,
                "reason": reason,
            }

            return render_to_response('donations/donate_success.html',
                                      template_values,
                                      request)

    else:
        form = AnonDonateForm()

    template_values.update({
        'form': form,
    })

    return render_to_response('donations/donate.html',
                              template_values, request)
