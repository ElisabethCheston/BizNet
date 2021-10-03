from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    ProfilesListView,
    NetworkProfileView,
)

urlpatterns = [
    # path('', views.network, name='network'),
    path('', ProfilesListView.as_view(), name='all_profiles'),
    path('network_profile_details/<int:pk>/', NetworkProfileView.as_view(), name='network_profile_details'),
    # path('', views.all_profiles, name='all_profiles'),
    path('contacts/', views.myContacts, name='contacts'),
    path('my_followers/', views.my_followers, name='my_followers'),
    path('following_ppl/', views.following_ppl, name='following_ppl'),
]