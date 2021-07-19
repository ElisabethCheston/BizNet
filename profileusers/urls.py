from django.urls import path
from . import views
from .views import (
    MyProfile,
    ProfileData,
)


urlpatterns = [
    path('', views.all_profiles, name='profiles'),
    path('my_profile/', views.MyProfile.as_view(), name='my_profile'), # .as_view() to "convert" a class-based view for url
    path('profile_data/', views.ProfileData.as_view(), name='profile_data'), # .as_view() to "convert" a class-based view for url
    path('profile_details/', views.profile_details, name='profile_details')
]

