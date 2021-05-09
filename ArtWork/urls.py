from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.View,name='View' ),
    path('Manage',views.Manage, name='Manage'),

    
]
