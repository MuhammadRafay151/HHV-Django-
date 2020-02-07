"""
Definition of urls for HHV_FABRICS.
"""
from datetime import datetime
from django.urls import path
from django.urls import include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from DashBoard import views as ds


urlpatterns = [
    path('Products/',include('Products.urls')),
    #path('', views.home, name='home'),
    path('',ds.index),
    path('Account/',include("Account.urls")),
    path('Dashboard/',include('DashBoard.urls')),
    path('Cart/',include('Cart.urls')),
    path('Order/',include('Order.urls')),
]
