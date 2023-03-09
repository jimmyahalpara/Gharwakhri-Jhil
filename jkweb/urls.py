"""jkweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import is_valid_path, include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from register import  views
# from accounts import  views
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/',include('accounts.urls')),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('loginin/', views.loginin, name='loginin'),
    path('logout/', views.logout, name='logout'),
    # # path('', views.registeruser, name='registeruser'),
    
    
    # path('shop-wishlist/',views.shopwish,name='shopwish'),
    # path('page-account/', views.pgaccount, name='pgaccount'),
    
    # path('page-contact/',views.pgcontact,name='pgcontact'),
    # path('page-pvt-policy/',views.pgpvtpolicy,name='pgpvtpolicy'),
    # path('page-purchase-guide/',views.purchaseguide,name='purchaseguide'),
    
    # path('shop-cart/',views.shopcart,name='shopcart'),
    
]
















# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('register/', views.showformdata, name='register'),
    
#     path('page-pglogin/', views.my_view, name='pglogin'),
#     path('page-register/', views.add_user, name='add_user'),
#     # path('page-loginin/', views.loginin, name='loginin'),    
#     path('page-about/', views.pgabout,name='pgabout'),
#     # path('page-register/', views.pgregister, name='pgregister'),
    
#     # path('blog-category-list/',views.blogcategorylist,name='blogcategorylist'),
#     # path('blog-post-left/', views.blogpostleft,name='blogpostleft'),
#     # path('blog-post-right/',views.blogpostright,name='blogpostright'),
    
    
#     path('page-account/', views.pgaccount, name='pgaccount'),
    
#     path('page-contact/',views.pgcontact,name='pgcontact'),
#     path('page-pvt-policy/',views.pgpvtpolicy,name='pgpvtpolicy'),
#     path('page-purchase-guide/',views.purchaseguide,name='purchaseguide'),
    
#     path('shop-cart/',views.shopcart,name='shopcart'),
#     # path('shop-compare/',views.shopcompare,name='shopcompare'),
#     # path('shop-grid-left/',views.shopgridleft,name='shopgridleft'),
#     # path('shop-invoice/',views.shopinvoice,name='shopinvoice'),
#     # path('shop-grid-right/',views.shopgridright,name='shopgridright'),
#     # path('shop-list-left/',views.shoplistleft,name='shoplistleft'),
#     # path('shop-list-right/',views.shoplistright,name='shoplistright'),
#     path('shop-wishlist/',views.shopwish,name='shopwish'),
    
# ]
