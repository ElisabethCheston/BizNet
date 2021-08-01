from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.network, name='network'),
    path('contacts/', views.myContacts, name='contacts'),
]