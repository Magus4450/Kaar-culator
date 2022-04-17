from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User = get_user_model()


class LoginForm(forms.Form):

    email = forms.CharField(max_length=150, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        }))
    password = forms.CharField(max_length=150, label='',  widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        }))
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='',  widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        }))
    last_name = forms.CharField(max_length=50, label='',  widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        }))

        
    email = forms.EmailField(max_length=100, label='',  widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        }))
    password = forms.CharField(max_length=150, label='',  widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        }))
    confirm_password = forms.CharField(max_length=150, label='',  widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        }))


    
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data
    
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Email already exists')
        return self.cleaned_data['email']
    
