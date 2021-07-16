from django.urls import path
from . import views

# from . import views

# app_name = 'profileusers'

urlpatterns = [
    path('', views.all_profiles, name='profiles'),
   path('profile_details/', views.profile_details, name='profile_details')
]
