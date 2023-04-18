from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [   
 path('login',views.login, name='login'),
 path('home', views.home, name='home'),
 path('directory', views.directory, name='directory'),
 path('annoucement', views.annoucement, name='annoucement'),
 path('request', views.request, name='request'),
 path('checkinn', views.checkinn, name='checkinn'),
 path('checkin', views.checkin, name='checkin'),
 path('checkout', views.checkout, name='checkout'),
 path('logout', views.logout, name='logout')
]
