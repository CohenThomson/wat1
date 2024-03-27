from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.models import User 
from users.models import UserProfile


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            messages.success(request, "Invalid Credentials.")
            return render(request, "users/login.html")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect(reverse('users:login'))

@login_required
def create_user(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=email, email=email, password=password, first_name=firstname, last_name=surname)
                   
            UserProfile.objects.create(
                user=user,
                firstname=firstname,  
                surname=surname,  
                email=email,  
                
            )
            
            return redirect('users:index')
    else:
        form = UserForm()

    return render(request, 'users/create_User.html', {'form': form})