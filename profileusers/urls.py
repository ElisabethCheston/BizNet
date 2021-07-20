from django.urls import path
from . import views
from .views import (
    MyProfile,
    ProfileData,
)


urlpatterns = [
    path('', views.all_profiles, name='profiles'),
    path('my-profile/', MyProfile.as_view(), name='my-profile'), # .as_view() to "convert" a class-based view for url
    path('profile-data/', ProfileData.as_view(), name='profile-data'), # .as_view() to "convert" a class-based view for url
    path('profile-details/', views.profile_details, name='profile-details')
]

