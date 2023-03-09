from django.urls import path
from . import views

urlpatterns=[
    path('login-user',views.login_user,name='loginuser'),
    path('register-user',views.register_user,name='registeruser'),
    
]