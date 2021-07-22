from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('network/', views.network, name='network'),
    path('my_contacts/', views.myContacts, name='my_contacts'),
]