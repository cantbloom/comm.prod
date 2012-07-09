from django import forms
from django.core import validators
from commProd.models import UserProfile, User

class RegForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'First Name'}), label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}), label="")
    shirt_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Shirt names!'}), label="")
    pic_url = forms.CharField(label="", required=False)
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder' : 'Password'}), label="" )
    password_confirm = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Password'}), label="")
    alt_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' : 'Alternative Email'}), label="", required=False)

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        
        if not password_confirm:
            raise forms.ValidationError("You must confirm your password")
        if password != password_confirm:
            raise forms.ValidationError("Your passwords do not match")
        return password

    def clean_alt_email(self):
        data = self.cleaned_data['alt_email']
        if UserProfile.objects.filter(email__email=data).exists() or User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data