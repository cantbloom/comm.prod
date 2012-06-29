from django import forms
from django.core import validators
from commProd.models import UserProfile
#from django.contrib.auth.models import User
 

class RegForm(forms.Form):
    first = forms.CharField()
    last = forms.CharField()
    shirt_name = forms.CharField()
    alt_email = forms.EmailField(required=False)
    password1 = forms.CharField( widget=forms.PasswordInput, label="Your Password" )
    password2 = forms.CharField( widget=forms.PasswordInput, label="Your Password")

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

    def clean_alt_email(self):
        data = self.cleaned_data['alt_email']
        if UserProfile.objects.filter(alt_email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
    
    # def save(self, new_data):
    #   u = UserProfile.objects.get(e)
    #   u.is_active = False
    #   u.save()
    #   return u