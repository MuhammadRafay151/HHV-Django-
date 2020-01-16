from django.urls import path
from .views import *
urlpatterns=[
    path('Add/',Add),
    path('showcart/',Showcart),
    path('Remove/',Remove),
    path('Deletecart/',Deletecart),
    path('Updatecart/',Updatecart),
    path('CBill/',CBill),
    path('Ckout/',CkOut),
]