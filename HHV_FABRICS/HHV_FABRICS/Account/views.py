from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from Products.DataBase import database
from Account import form,models
# Create your views here.
def Login(request):
    if request.method=="POST":
        up=form.Login(request.POST)
        if up.is_valid():
            u1=models.User()
            x=u1.Authenticate(request.POST.get('UserName'),request.POST.get('Password'))
           
            if x==True:
               request.session['User'] = u1.GetUserId(request.POST.get('UserName'))
               return HttpResponseRedirect('/Products/')
        return HttpResponseRedirect('/')
def  SignUp(request):
     pass
def Logout(request):
    del request.session['User']
    return HttpResponseRedirect('/')
