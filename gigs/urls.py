from django.urls import path
from . import views
from .views import gig, gig_json

#app_name = 'gigs'

urlpatterns = [
    path('', views.gig, name='gig'),

    # endpoints
    path('gigs-json/', gig_json, name='gig-json'),
]