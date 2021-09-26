from django.urls import path
from . import views
from .views import GigListView, GigCreateView, GigDetailView, gig_json
from .views import (gig_json)


# ListView = <app>/<model>_<viewtyp>.html

urlpatterns = [
    path('', GigListView.as_view(), name='gig'),
    path('gig/<int:pk>/', GigDetailView.as_view(), name='gig_detail'),

    path('create_gig/', GigCreateView.as_view(), name='create_gig'),
    path('my_gigs/', views.my_gigs, name='my_gigs'),

    path('new_gig/', views.NewGig, name='new_gig'),
    path('saved_gig/', views.SavedGig, name='saved_gig'),
    path('apply_gig/', views.AppliedGig, name='apply_gig'),
    path('hide_gig/', views.HideGig, name='hide_gig'),
     
    path('gig_json/', gig_json, name='gig_json'), # endpoints
]