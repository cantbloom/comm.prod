from django import forms
from django.core import validators
from donations.models import *

from datetime import datetime

class DonateForm(forms.Form):
    RUSH = 'Rush/anti-rush week'
    DTYD = 'DTYD'
    GEN_FUN = 'General floor donation'
    DONATION_CHOICES = (
        (RUSH, RUSH),
        (GEN_FUN, GEN_FUN),
        (DTYD, DTYD),
    )
    reason = forms.ChoiceField(choices=DONATION_CHOICES)
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'span1'}), label="")
    is_anonymous = forms.BooleanField(required=False, label="Anonymous Donation?")

