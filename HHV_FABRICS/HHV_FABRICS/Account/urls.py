from django.urls import path
from . import views
urlpatterns=[
    path('signup/',views.SignUp),
    path('login/',views.Login),
    path('logoff/',views.Logout)
    ]


