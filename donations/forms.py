from django import forms
from django.core import validators
from donations.models import *

from datetime import datetime

class DonateForm(forms.Form):
    """
    Take a donation from a user with an account.
    """
    ABC = 'ABC Party ($10)'
    GEN_FUN = 'General floor donation'
    DONATION_CHOICES = (
        (ABC, ABC),
        (GEN_FUN, GEN_FUN),
    )
    reason = forms.ChoiceField(choices=DONATION_CHOICES)
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'span1', "autocomplete" : "off"}), label="")
    is_anonymous = forms.BooleanField(required=False, label="Anonymous Donation?")

class AnonDonateForm(forms.Form):
    
    """ 
    Anonymous donation form.
    """
    reason = forms.CharField(widget=forms.TextInput(attrs={ "autocomplete" : "off"}), label="")
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'span1', "autocomplete" : "off"}), label="")
