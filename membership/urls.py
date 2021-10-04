from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_profile, name='membership_profile')
]
