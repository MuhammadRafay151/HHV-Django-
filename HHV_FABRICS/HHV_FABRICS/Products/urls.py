from django.urls import path
from . import views

urlpatterns = [

    path('ViewProducts/', views.ViewProduct, name='index'),
    path('check/', views.check, name='index'),
    path('AddProducts/', views.AddProducts, name='pro'),
    path('SubmitProduct/', views.SubmitProduct, name='ssdsd'),
    path('Form/',views.Form,name='FORM'),
  
]
