from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_profiles, name='profiles'),
    path('profile_details/', views.profile_details, name='profile_details')
]