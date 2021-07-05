from django.urls import path
from . import views

urlpatterns = [
    path('profileusers/', views.profile, name='profile')
]
