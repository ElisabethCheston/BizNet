from django.urls import path
from . import views
from .views import (
    GigListView, 
    GigCreateView, 
    GigDetailView, 
    gig_json,
    GigUpdateView,
    GigDeleteView,
)


# ListView = <app>/<model>_<viewtyp>.html

urlpatterns = [
    path('', GigListView.as_view(), name='gig'),
    path('gig/<int:pk>/', GigDetailView.as_view(), name='gig_detail'),
    path('gig/<int:pk>/update/', GigUpdateView.as_view(), name='gig_update'),
    path('gig/<int:pk>/delete/', GigDeleteView.as_view(), name='gig_confirm_delete'),

    path('new/', GigCreateView.as_view(), name='create_gig'),
    path('my_gigs/', views.my_gigs, name='my_gigs'),

    # path('new_gig/', views.NewGig, name='new_gig'),
    path('saved_gig/', views.SavedGig, name='saved_gig'),
    path('apply_gig/', views.AppliedGig, name='apply_gig'),
    path('hide_gig/', views.HideGig, name='hide_gig'),
     
    path('gig_json/', gig_json, name='gig_json'), # endpoints
]