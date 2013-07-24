from django import forms

DEFAULT_ATTRS = {
            'class' : 'span1', 
            "autocomplete" : "off", 
            "placeholder" : "33"
            }

class DonateForm(forms.Form):
    """
    Take a donation from a user with an account.
    """
    # ABC = 'ABC'
    # HOLIDAY = 'Holiday Party'
    SPEAK = "Speakeasy"
    DTYD = "DTYD"
    GEN_FUN = 'General floor donation'
    DONATION_CHOICES = (
        (DTYD, DTYD),
        (SPEAK, SPEAK),
        (GEN_FUN, GEN_FUN),
    )
    reason = forms.ChoiceField(choices=DONATION_CHOICES)
    amount = forms.IntegerField(widget=forms.TextInput(
        attrs=DEFAULT_ATTRS), label="")
    is_anonymous = forms.BooleanField(required=False, 
        label="Anonymous Donation?")

class AnonDonateForm(forms.Form):
    
    """ 
        Anonymous donation form.
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "autocomplete" : "off", 
            "placeholder" : "Anonymous"
        }), label="")
    reason = forms.CharField(
        widget=forms.TextInput(attrs={
            "autocomplete" : "off",
            "placeholder" : "DTYD"
            }), label="")
    amount = forms.IntegerField(
        widget=forms.TextInput(attrs=DEFAULT_ATTRS),
        label="")
