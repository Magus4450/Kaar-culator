from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):

    email = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=150, widget=forms.PasswordInput())


    
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data
    
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Email already exists')
        return self.cleaned_data['email']
    
