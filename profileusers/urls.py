from django.urls import path
from .views import profile_view

# from . import views

app_name = 'profileusers'

urlpatterns = [
<<<<<<< HEAD
    path('test/', profile_view, name='profile')
]
=======
    path('', views.all_profiles, name='profiles'),
    path('profile_details/', views.profile_details, name='profile_details')
]
>>>>>>> 488e657 (Recover project files and update migrations.)
