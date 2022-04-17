import email
from re import M
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from .models import User




def login_view(request):

    if request.method == 'POST':
        # Make a instance of login form with POST data
        form = LoginForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Check if username and password matches
            user = authenticate(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            print(user)
            # If user exists with that username and password
            if user:

                # login the user
                login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                # redirect to their profile
                return redirect(reverse_lazy('home:home'))
            else:
                print("Creds do not match")
        else:
            print("FORM INVALID")
    
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home:home'))

        form = LoginForm()

    return render(request, 'templates/accounts/login.html', {'form': form})



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password'],                
            )

            # send_email(user)
            # return render(request, 'templates/email/confirm_template.html')

            

            # To encrypt the password
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse_lazy('home:home'))
    elif request.method == "GET":
        form = RegisterForm()

    return render(request, 'templates/accounts/register.html', {'form': form})

@login_required(login_url=reverse_lazy('accounts:login'))
def profile_view(request):
    user = request.user

    return render(request, 'templates/accounts/account.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home:home'))

