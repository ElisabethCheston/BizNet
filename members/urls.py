from django.urls import path
from . import views


urlpatterns = [
    path('members/', views.get_member_profile, name='member')
]
