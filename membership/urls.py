from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_profile, name='membership_profile'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('my_subscription/', views.my_subscription, name='my_subscription'),
    path('payment_histrory/', views.payment_histrory, name='payment_histrory'),
]
