from django.shortcuts import render
from .models import Order
# Create your views here.
def ViewOrders(request):
    o1=Order()
    x=o1.GetOrder(request.session.get('User'))
    return render(request,"Order/Index.html",{'data':x})
def OrderDetails(request):
    o1=Order()
    x=o1.OrderDetail(request.session.get('User'),request.GET.get('billno'))
    print(x)
    return render(request,'Order/Details.html',{'data':x})

