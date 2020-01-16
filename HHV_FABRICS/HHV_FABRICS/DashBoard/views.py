from django.shortcuts import render
from Account import form
from Account.UserBusinessLayer import UserBusinessLayer
# Create your views here.
def index(request):
    d1=UserBusinessLayer()
    de=d1.GetDealers();
    ac=d1.GetAccountTypes();
    login_form= form.Login()
    return render(request,"DashBoard/Index.html",{"form": login_form,"de":de,"ac":ac})
def About(request):
    return render(request,'DashBoard/About.html')