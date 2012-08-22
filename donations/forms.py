from django import forms
from django.core import validators
from donations.models import *

from datetime import datetime

class DonateForm(forms.Form):
    RUSH = 'Rush/anti-rush week'
    DTYD = 'DTYD'
    GEN_FUN = 'General floor donation'
    PARTY = 'Any party throughout the year'
    DONATION_CHOICES = (
        (DTYD, DTYD),
        (GEN_FUN, GEN_FUN),
        (RUSH, RUSH),
        (PARTY, PARTY),
    )
    reason = models.CharField(max_length=2, choices=DONATION_CHOICES, default=RUSH)
    amount = forms.FloatField(widget=forms.TextInput(attrs={'placeholder' : 'Amount', 'class': 'fancy-input'}), label="")
    is_anonymous = forms.BooleanField(required=False)

