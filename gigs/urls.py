from django.urls import path
from . import views
from .views import gig, gigs_json

# app_name = 'gigs'


urlpatterns = [
    path('', gig, name='gig'),

    # endpoints
    path('gigs-json/', gigs_json, name='gigs-json'),
]