from django.db import models
from Products.DataBase import database
# Create your models here.
class Dealer:
    Type=""
    id=0

class User:
    Name=""
    UserName=""
    IsAdmin=False
    def Authenticate(self,username,password):
        Querry="select * from Users where UserName='{}' and Password='{}' ".format(username,password)
        d1=database()
        x=d1.read(Querry)
        if len(x)==1:
            return True
        else:
            return False
    
    def ReadUser():
        Querry=""
        d1=database()
        x=d1.read(Querry)
        self.Name=x
        self.UserName

    def GetUserId(self,username):
        Querry="select UserId from Users where UserName='{}'".format(username)
        d1=database()
        x=d1.read(Querry)
        return x[0][0]
     