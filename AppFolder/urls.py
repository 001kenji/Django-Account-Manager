from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('login/', views.LoginUser),
    path('logged', views.loggedUser),
    path('logOut', views.loggingOut),
]