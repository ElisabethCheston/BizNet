from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.network, name='network'),
    path('contacts/', views.myContacts, name='contacts'),
    path('my_followers/', views.my_followers, name='my_followers'),
    path('following_ppl/', views.following_ppl, name='following_ppl'),

]