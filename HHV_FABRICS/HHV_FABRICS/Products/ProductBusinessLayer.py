from Products.DataBase import database
from Products.models import Product
class ProductBusinessLayer(object):
    def GetProductList(self):
        d1=database()

        Querry2="select [Product ID],[Product Name],Image from product"
        data=d1.read(Querry2)
        data=self.GenerateProductView(data)
        return data
      
    def GenerateProductView(self,data):
        #algo to arrange items in 2d list or list of lists
        
        list2=[]
        i=0
        print(len(data))
        while(i<len(data)):
            list1=[]
            j=0
            while(j<4 and i<len(data)):
                list1.append(data[i])
                j+=1
                i+=1 
            list2.append(list1)
        return list2
    
           
       