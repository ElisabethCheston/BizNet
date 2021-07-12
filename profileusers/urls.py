from django.urls import path
from .views import profile_view

# from . import views

app_name = 'profileusers'

urlpatterns = [
    path('test/', profile_view, name='profile')
]
