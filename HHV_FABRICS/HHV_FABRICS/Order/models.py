from django.db import models
from Products.DataBase import database
class Order():
    def GetOrder(self,uid):
        Querry="select * from CustomerOrder where CustomerId="+str(uid)
        d1=database()
        x=d1.read(Querry)
        return x
    def OrderDetail(self,uid,billno):
        d1=database()
        Querry='''SET NOCOUNT ON; exec OrderDetail {},{} '''.format(uid,billno)
        x=d1.read(Querry)
        return x
