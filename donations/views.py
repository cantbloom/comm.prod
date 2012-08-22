from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

"""
Donation home page. Return all of the donation objects that are found.
"""
@login_required
def home(request):
    donations = Donation.objects.order_by('date')
    template_values = {
        'page_title' : "Donations",
        'nav_donations' : "active",
    }

    return render_to_response('donate/home.html', template_values, context_instance=RequestContext(request))

"""
Donate page returns the form for submitting a donation
"""
@login_required
def donate(request):
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            amount = form.cleaned_data['amount']
            is_anonymous = form.cleaned_data['is_anonymous']
            user_profile = request.user.profile
    else:
        form = DonateForm()
        template_values = {
            'page_title' : "Make a Donation",
            'nav_donations' : "active",
        }

    return render_to_response('donate/donate.html', template_values, context_instance=RequestContext(request))