from django.urls import path
from . import views

urlpatterns = [

    path('', views.ViewProduct, name='index'),
    path('check/', views.check, ),
    path('Image/', views.Image, ),
    path('ProductDetails/',views.ProductDetails,),
    path('AddProducts/', views.AddProducts, name='pro'),
    path('SubmitProduct/', views.SubmitProduct, name='ssdsd'),
    path('Form/',views.Form,name='FORM'),
  
]
