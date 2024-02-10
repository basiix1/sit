from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegisterForm


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('main:home')
        else:
            return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/profile.html')


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('main:home')
        return render(request,'accounts/login.html')
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('main:home')
        
        return render(request,'accounts/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')