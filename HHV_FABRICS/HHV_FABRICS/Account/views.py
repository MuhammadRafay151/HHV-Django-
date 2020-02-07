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
               request.session['User'] =u1.Uid
               request.session['Name']=u1.Name
               request.session['ImgId']=u1.Imgid
               request.session['IsAdmin']=u1.IsAdmin
               return HttpResponseRedirect('/Products/')
        return HttpResponseRedirect('/')
def  SignUp(request):
     if request.method=='POST': 
         f1=form.Signup(request.POST,request.FILES)
         if f1.is_valid():
             s1=models.User()
             s1.RegisterNewUser(f1)
             request.session['User'] =s1.Uid
             request.session['Name']=s1.Name
             request.session['ImgId']=s1.Imgid
             request.session['IsAdmin']=s1.IsAdmin
         else:
             print(request.POST)
          

     return HttpResponseRedirect('/')       

def Logout(request):
    del request.session['User']
    del request.session['Name']
    del request.session['ImgId']
    del request.session['IsAdmin']
    return HttpResponseRedirect('/')
