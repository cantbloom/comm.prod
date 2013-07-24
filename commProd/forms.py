from django import forms
import commProd.models as cpm

from datetime import datetime

class RegForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder' : 'First Name', 
            'class': 'fancy-input'
            }), label="")
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder' : 'Last Name', 
            'class': 'fancy-input'
            }), label="")
    class_year = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder':'1933', 
            'class': 'fancy-input'
            }), label="")
    pic_url = forms.CharField(label="", required=False)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder' : 'Password', 
            'class': 'fancy-input'
            }), label="" )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder' : 'Confirm Password',
            'class': 'fancy-input'
            }), label="")
    alt_email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder' : 'Alternative Email', 
            'class': 'fancy-input'
            }), label="", required=False)

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        
        if not password_confirm:
            raise forms.ValidationError(
                "You must confirm your password")
        if password != password_confirm:
            raise forms.ValidationError(
                "Your passwords do not match")
        return password

    def clean_alt_email(self):
        data = self.cleaned_data['alt_email']
        if cpm.UserProfile.objects.filter(
            email__email=data, email__confirmed=True).exists() \
        or cpm.UserProfile.objects.filter(user__email=data, 
            send_mail=True).exists():
            raise forms.ValidationError('Email already in use.')
        return data

    def clean_class_year(self):
        try:
            class_year = int(self.cleaned_data['class_year'])
            max_year = datetime.today().year + 4
            if not class_year in range(1933, max_year + 1):
                raise forms.ValidationError(
                    'Enter a class year between 1933 and %s' % max_year)
        except ValueError:
            raise forms.ValidationError(
                'Enter a class year between 1933 and %s' % max_year)
        return class_year

