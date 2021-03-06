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
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        

        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
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

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        user.set_password(self.cleaned_data['password'])

        user.save()

        return user

    def clean(self):
        print(self.cleaned_data.get('password'))
        print(self.cleaned_data.get('confirm_password'))
        if self.cleaned_data.get('password') != self.cleaned_data['confirm_password']:
            raise forms.ValidationError('Passwords do not match')
        elif len(self.cleaned_data['password']) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        elif not any(char.isdigit() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one number')
        elif not any(char.isupper() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one uppercase letter')
        elif not any(char.islower() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one lowercase letter')
        elif not any(char.isalpha() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one letter')
        elif self.cleaned_data['first_name'] in self.cleaned_data['password']:
            raise forms.ValidationError('Password cannot contain first name')
        elif self.cleaned_data['last_name'] in self.cleaned_data['password']:
            raise forms.ValidationError('Password cannot contain last name')
        
        return self.cleaned_data
    


    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Email already exists')
        return self.cleaned_data['email']


