from django import forms
from .models import Feedback


class FeedbackForm(forms.Form):

    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'class': 'form-control border-0',
        }))
    
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control border-0',
        }))

    message = forms.CharField(max_length=1000, label='', widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'class': 'form-control border-0',
        'rows': '5',
        'cols': '10',
        }))
    

    def save(self, commit=True):
        feedback = Feedback.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            message=self.cleaned_data['message'],
        )
        feedback.save()
        return feedback
                                         


    