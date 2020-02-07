from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from .DataBase import database
from . import Forms
from .models import *
import json
from Products.ProductBusinessLayer import ProductBusinessLayer
# from DB import test

# Create your views here.

def ViewProduct(request):
   
    p1=ProductBusinessLayer()
    data=p1.GetProductList()
    return render(request, 'Products/View_Products.html',{'data':data,'range1':range(3),'range2':range(5)})

def AddProducts(request):
    if('IsAdmin'in request.session and request.session['IsAdmin']==True):
          t1 = database()
          color = t1.read("select * from color")
          fabrics = t1.read("select * from fabric")
          Designs = t1.read("select * from designs")
          return render(request, 'Products/AddProducts.html', {'data': color, 'fabric': fabrics, 'Designs': Designs})
    else:
        return HttpResponseRedirect('/')
   
def Image(request):
    if(request.GET.get("id")!=""):
       p1=Product()
       img=p1.GetProductImage(request.GET.get("id"))
       
       return HttpResponse(img[1], content_type="image/jpg")
    else:
        raise Http404("Poll does not exist")
def ProductDetails(request):
   p1=Product()
   x=request.GET.get("id")
   p1.LoadDetails(x) 
   return JsonResponse(p1.__dict__,safe=False)

def SubmitProduct(request):
    if request.method == 'POST':
        form=Forms.Product(request.POST, request.FILES)
        if form.is_valid():
            p1=Product()
            p1.InsertProduct(form)
            return HttpResponseRedirect('/Products/AddProducts')
        else:
            return HttpResponse("Some thing going wrong try again later")

        
    else:
        return HttpResponseRedirect('/Products/AddProducts')


def check(request):
    t1 = database()
    data = t1.read("select * from employee")
    return HttpResponse(data[0][0])

def Form(request):
    if request.method=='POST':
        fm=TestForm(request.POST)
        if fm.is_valid():
            return HttpResponse(fm.cleaned_data['text'])
    fm=TestForm()
    return render(request,'Products/form.html',{'form':fm})
