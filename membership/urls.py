from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_profile, name='membership_profile'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('my_subscription/', views.my_subscription, name='my_subscription'),
    # Stripe
    path('payment_histrory/', views.payment_histrory, name='payment_histrory'),
    path("config/", views.stripe_config),
    path("create-checkout-session/", views.create_checkout_session),
    path("success/", views.memership_success, name='memership_success'),
    path("cancel/", views.memership_cancel, name='memership_cancel'),
]
