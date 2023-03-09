from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm

def register_user(request):
    if request.method == 'POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid()
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Success"))
            return redirect('home')
        else:
            form=RegisterUserForm()
            return render(request,'page-register.html',{'form',form})

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get['username']
        password=request.POST.get['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('loginuser')
            messages.success(request,("Not a user")
    else:
        return render(request,'page-login.html')