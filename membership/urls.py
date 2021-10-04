from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_membership_profile, name='membership')
]
