from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from Products.models import Product
from .models import Cart
# Create your views here.

def Add(request):
    if 'User' in request.session:
        message=""
        c1=Cart()
        try:
           c1.AddToCart(request.session.get('User'),request.GET.get('Pid'),request.GET.get('Qty'))
           message="Added To cart!"
        except OverflowError:
          message="quantity you enterd not in stock"
        message={"Mes":message,"check":"true"}
    return JsonResponse(message,safe=False)

def Remove(request):
     if 'User' in request.session:
        c1=Cart()
        c1.RemoveFromCart(request.session.get('User'),request.GET.get('Pid'))
     return redirect('/Cart/showcart/')
def Showcart(request):
    if 'User' in request.session: 
        c1=Cart()
        list=c1.GetCart(request.session.get('User'))
    return render(request,"cart/cart.html",{"data":list})

def Deletecart(request):
    c1=Cart()
    c1.RemoveCart(request.session.get('User'))
    return redirect('/Cart/showcart/')
def Updatecart(request):
    c1=Cart()
    c1.UpdateCart(request.session.get('User'),request.GET.get('Pid'),request.GET.get('Qty'))
    return redirect('/Cart/showcart/')
def CBill(request):
    c1=Cart()
    x=c1.calculatebill(request.session.get('User'))
    return JsonResponse(x,safe=False)    
def CkOut(request):
    c1=Cart()
    c1.checkoutcart(request.session.get('User'))
    return redirect('/Cart/showcart/')
def CkQty(request):
    c1=Cart()
    x=c1.CheckQty(request.session.get('User'))
    return JsonResponse(x,safe=False)
