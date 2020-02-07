from django.db import models
from Products.DataBase import database
# Create your models here.
class Cart:
    def IsInStock(self,ProductId,Qty):
        querry="select [Quantity in Stock] from Product where [Product ID]="+ProductId
        d1=database()
        x=d1.read(querry)
        x=int(x[0][0])
        if x < int(Qty):
            return False
        else:
           return True
    def AddToCart(self,userid,ProductId,Qty):
        check=self.IsInStock(ProductId,Qty)
        if check:
         querry='''exec cartupdate %s,%s,%s'''
         ProductId=int(ProductId)
         Qty=int(Qty)
         data=(userid,ProductId,Qty,)
         d1=database()
         d1.Insert(querry,data)
        else:
         raise OverflowError("Quantity out of range") 
        
        return None
        
    def RemoveFromCart(self,userid,ProductId):
        querry="delete from Cart where UserId='{}' and ProductId='{}'".format(userid,ProductId)
        ProductId=int(ProductId)
        d1=database()
        d1.Delete(querry)
        return None
        
    def UpdateCart(self,userid,ProductId,Qty):
        querry='''update Cart set Qunatity=%s where UserId=%s and ProductId=%s'''
        ProductId=int(ProductId)
        Qty=int(Qty)
        data=(Qty,userid,ProductId,)
        d1=database()
        d1.Update(querry,data)
        return None
    def RemoveCart(self,userid):
        querry="delete from Cart where UserId='{}'".format(userid)
        d1=database()
        d1.Delete(querry)
        return None
    def GetCart(self,userid):
        querry='''
        select Product.[Product ID],Product.[Product Name],Cart.Qunatity,Image from cart inner join Product on Product.[Product ID]=Cart.ProductId where UserId={}
     '''.format(userid)
        d1=database()
        x=d1.read(querry)
        return x
    def calculatebill(self,uid):
     querry="select FORMAT(sum(Product.[Product Price]*Cart.Qunatity), 'c', 'en-pk')as TotalBill from Cart inner join  Product on Cart.ProductId=Product.[Product ID] where Cart.UserId="+str(uid)
     d1=database()
     x=d1.read(querry)
     return x[0][0]
    def checkoutcart(self,userid):
        querry='''exec checkoutcart %s'''
        data=(userid,)
        d1=database()
        x=d1.Insert(querry,data)
        return None
    def CheckQty(self,uid):
        list=[]
       
        querry='''Select Cart.ProductId,Cart.Qunatity,Product.[Product ID],Product.[Quantity in Stock],Product.[Product Name] from Cart inner join Product on Product.[Product ID]=Cart.ProductId where UserId={}'''.format(uid)
        d1=database()
        x=d1.read(querry)
        for i in x:
            if i[1]>i[3]:
                list2=[]
                list2.append(i[4])
                list2.append("Only {} pieces available in stock".format(i[3]))
                list.append(list2)
        return list        