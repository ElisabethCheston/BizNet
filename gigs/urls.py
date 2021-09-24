from django.urls import path
from . import views
from .views import (gig, gig_json)


# app_name = 'gigs'


urlpatterns = [
    path('', gig, name='gig'),
    path('new_gig/', views.NewGig, name='new_gig'),
    path('saved_gig/', views.SavedGig, name='saved_gig'),
    path('apply_gig/', views.AppliedGig, name='apply_gig'),
    path('hide_gig/', views.HideGig, name='hide_gig'),
     
    path('gig_json/', gig_json, name='gig_json'), # endpoints
]