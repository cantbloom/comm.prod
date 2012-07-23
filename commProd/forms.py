from django import forms
from django.core import validators
from commProd.models import UserProfile, User
from helpers.aws_put import put_profile_pic

import datetime

class RegForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'First Name'}), label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}), label="")
    class_year = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'1933'}), label="")
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
        if UserProfile.objects.filter(email__email=data, email__confirmed=True).exists() or UserProfile.objects.filter(user__email=data, send_mail=True).exists():
            raise forms.ValidationError('Email already in use.')
        return data

    def clean_class_year(self):
        try:
            class_year = int(self.cleaned_data['class_year'])
            max_year = datetime.datetime.today().year + 4
            if not class_year in range(1933, max_year):
                raise forms.ValidationError('Enter a class year between 1933 and %s'%max_year)
        except ValueError:
            raise forms.ValidationError('Enter a class year between 1933 and %s'%max_year)
        return class_year

