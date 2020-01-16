from django.db import models
from Products.DataBase import database
import json

class Product():
   id=""
   #def GenerateJson(self):
   #   self.JsonString=json.dumps(self.__dict__)
   def GetProductImage(self,id):
       querry="select * from Images where id=%s"
       data=(id,)
       t1=database()
       img=t1.read_p(querry,data)
       return img[0]
   def LoadDetails(self,id):
       d1=database()
       Querry='''select Product.[Product Name],Designs.DesignName,Color.color ,Product.[Number Of Pieces]
       ,Product.[Quantity in Stock],Product.[Product Price]
       ,x.Fabric,y.Fabric,Fabric.Fabric,Product.IsKameezFrontEmbroided,Product.IsKameezBackEmbroided
       ,Product.IsDupattaEmbroided,Product.IsShalwarEmbroided from Product inner join color on Color.id=Product.Color 
       inner join Designs on Product.[Design Code]=Designs.DesignCode
inner join 
Fabric  on Fabric.id=Product.[Dupatta Fabric]inner join 
Fabric as x on x.id=Product.[Kameez Fabric]inner join 
Fabric as y on y.id=Product.[Shalwar Fabric] where [Product ID]='''+id
       print(Querry)
       x=d1.read(Querry)
       self.PName=x[0][0]
       self.Design=x[0][1]
       self.color=x[0][2]
       self.NPieces=x[0][3]
       self.Qstock=x[0][4]
       self.Price=x[0][5]
       self.KFabric=x[0][6]
       self.SFabric=x[0][7]
       self.DFabric=x[0][8]
       self.IsKameezFront=x[0][9]
       self.IsKameezBack=x[0][10]
       self.IsDupatta=x[0][11]
       self.IsShalwar=x[0][12]
   
   def InsertProduct(self,form):
     self.PName = form.cleaned_data.get('PName')
     self.Design = form.cleaned_data.get('Design')
     self.NPieces = form.cleaned_data.get('NPieces')
     self.Qstock = form.cleaned_data.get('Qstock')
     self.Price = form.cleaned_data.get('Price')
     self.color = form.cleaned_data.get('color')
     self.KFabric = form.cleaned_data.get('KFabric')
     self.SFabric = form.cleaned_data.get('SFabric')
     self.DFabric = form.cleaned_data.get('DFabric')
     self.IsKameezFront = form.cleaned_data.get('IsKameezFront')
     self.IsKameezBack = form.cleaned_data.get('IsKameezBack')
     self.IsDupatta = form.cleaned_data.get('IsDupatta')
     self.IsShalwar = form.cleaned_data.get('IsShalwar')
     self.Image=form.cleaned_data.get('Image')
     ImageByte=self.Image.read()
     t1 = database()
     querry='''set nocount on; insert into Images (Image) values (%s);
     select SCOPE_IDENTITY() as id'''
     data=(ImageByte,)
     id=t1.Insert_ReadId(querry,data)
     data=(self.PName,self.Design,self.NPieces,self.Qstock,self.Price,self.color,self.KFabric,self.SFabric,self.DFabric,self.IsKameezFront,self.IsKameezBack,self.IsDupatta,self.IsShalwar,id)
     querry='''insert into Product([Product Name],[Design Code],[Number Of Pieces]
,[Quantity in Stock],[Product Price],Color,[Kameez Fabric],[Shalwar Fabric],
[Dupatta Fabric],IsKameezFrontEmbroided,IsKameezBackEmbroided
,IsDupattaEmbroided,IsShalwarEmbroided,Image
) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
     t1.Insert(querry,data)
   



   
     
      
      

