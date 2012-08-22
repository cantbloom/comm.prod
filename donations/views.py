from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from helpers.renderers import donation_renderer

from donations.forms import DonateForm
from donations.models import *

"""
Donation home page. Return all of the donation objects that are found.
"""
@login_required
def home(request):
    donations = Donation.objects.order_by('-date')
    page = request.GET.get('page',1)
    donations = donation_renderer(donations, page)
    template_values = {
        'page_title' : "Past Donations",
        'nav_donate' : "active",
        'donation_timeline' : donations,
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
    }

    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            amount = form.cleaned_data['amount']
            is_anonymous = form.cleaned_data['is_anonymous']
            user_profile = request.user.profile

            donation = Donation(reason=reason, amount=amount, is_anonymous=is_anonymous, user_profile=user_profile)
            donation.save()

            return render_to_response('donations/donate_success.html', template_values, context_instance=RequestContext(request))

    else:
        form = DonateForm()

    template_values['form'] = form

    return render_to_response('donations/donate.html', template_values, context_instance=RequestContext(request))