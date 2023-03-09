# from django.shortcuts import render
# from django.contrib.auth.models import User, auth

# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .models import CustomUser
# from .forms import SignUpForm


# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from .forms import MyUserCreationForm

# def signup(request):
#     if request.method == 'POST':
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = MyUserCreationForm()
#     return render(request, 'page-register.html', {'form': form})

# def home(request):
#     return render(request, 'index-3.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import MyUserCreationForm
from .models import MyUser

@login_required
def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Do something with the user object or redirect to success page
            login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
    return render(request, 'page-register.html', {'form': form})



    
# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = CustomUser.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password1'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 phone_number=form.cleaned_data['phone_number'],
#                 city=form.cleaned_data['city'],
#                 question=form.cleaned_data['question'],
#                 answer=form.cleaned_data['answer'],
#                 role=form.cleaned_data['role']
#             )
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'register.html', {'form': form})


