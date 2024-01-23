from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.LoginUser),
    path('logged', views.loggedUser),
    path('logOut', views.loggingOut),
]