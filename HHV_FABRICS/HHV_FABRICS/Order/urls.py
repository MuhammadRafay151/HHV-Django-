from django.urls import path
from .views import *
urlpatterns=[
    path('',ViewOrders),
    path('Details/',OrderDetails),
]