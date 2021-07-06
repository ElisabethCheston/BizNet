from django.urls import path
from . import views
from .views import gig

urlpatterns = [
    path('', views.gig, name='gig')
]