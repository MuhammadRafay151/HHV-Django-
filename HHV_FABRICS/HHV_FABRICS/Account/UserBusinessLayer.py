from .models import Dealer
from Products.DataBase import database
class UserBusinessLayer(object):
   def GetDealers(self):
       d1=database()
       querry="select * from DealerTypes"
       x=d1.read(querry)
       return x
   def GetAccountTypes(self):
       d1=database()
       querry="select * from AccountType"
       x=d1.read(querry)
       return x



