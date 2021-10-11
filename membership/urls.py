from django.urls import path
from . import views 
from .views import (
    MembershipSelectView,
    )


urlpatterns = [
    path('', views.membership_profile, name='membership_profile'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('user_subscription/', views.get_user_subscription, name='user_subscription'),
    path('user_membership/', views.get_user_membership, name='user_membership'),
    path('', MembershipSelectView.as_view(), name='my_membership'),


    # Stripe
    path('payment_histrory/', views.payment_histrory, name='payment_histrory'),
    path("config/", views.stripe_config),
    # path("create-checkout-session/", views.create_checkout_session),
    path("success/", views.memership_success, name='memership_success'),
    path("cancel/", views.memership_cancel, name='memership_cancel'),
    # path("webhook/", views.stripe_webhook, name='stripe_webhook'),
]
