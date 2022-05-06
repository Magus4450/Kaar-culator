import email
from re import M
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from .models import User
from verify_email.email_handler import send_verification_email
from tax.models import TaxReceipt

from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)

            return render(request, 'templates/accounts/register.html', {'info': "Confirmation email has been sent. Please check you email", "form": form})
   
            # return redirect(reverse_lazy('home:home'))
    elif request.method == "GET":
        form = RegisterForm()

    return render(request, 'templates/accounts/register.html', {'form': form})

@login_required(login_url=reverse_lazy('accounts:login'))
def profile_view(request):
    user = request.user
    tax_receipts = TaxReceipt.objects.filter(user=user)
    users = User.objects.all()
    return render(request, 'templates/accounts/account.html', {'user': user, 'tax_receipts': tax_receipts, 'users': users})

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home:home'))


def deactivate_view(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect(reverse_lazy('accounts:account'))

def activate_view(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return redirect(reverse_lazy('accounts:account'))



