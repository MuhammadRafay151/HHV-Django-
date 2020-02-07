from django.db import models
from Products.DataBase import database
# Create your models here.
class Dealer:
    Type=""
    id=0

class User:
    Name=""
    Contact=""
    UserName=""
    Password=""

    IsAdmin=False
    def Authenticate(self,username,password):
        Querry="select * from Users where UserName='{}' and Password='{}' ".format(username,password)
        d1=database()
        x=d1.read(Querry)
        if len(x)==1:
            self.ReadUser(x)
            return True
        else:
            return False
    
    def ReadUser(self,x):
        self.Uid=x[0][0]
        self.Name=x[0][1]
        self.IsAdmin=bool(x[0][8])
        self.Imgid=x[0][6]


    def GetUserId(self,username):
        Querry="select UserId from Users where UserName='{}'".format(username)
        d1=database()
        x=d1.read(Querry)
        return x[0][0]
    
    def RegisterNewUser(self,form):
        self.Name=form.cleaned_data.get('Name')
        self.Contact=form.cleaned_data.get('Contact')
        self.UserName=form.cleaned_data.get('UserName')
        self.Password=form.cleaned_data.get('Password')
        self.Image=form.cleaned_data.get('Image')
        imgbytes=self.Image.read()
        data=(self.Name,self.UserName,self.Password,self.Contact,imgbytes,)
        Querry="exec RegisterUser %s,%s,%s,%s,%s"
        d1=database()
        id=d1.Insert(Querry,data)
        self.Authenticate(self.UserName,self.Password)
        return None
       