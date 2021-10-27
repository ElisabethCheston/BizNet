from django.urls import path
from . import views 
from .views import (
    MembershipSelectView,
    PaymentView,
    CreateCheckoutSession,
    updateTransactionRecords,
    )


urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('membership_profile', views.membership_profile, name='membership_profile'),
    # path('subscription/', views.Subscription, name='subscription'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', updateTransactionRecords, name='update-transactions'),


    # path('membership_list/', views.membership_list, name='membership_list'),

    # path('user_subscription/', views.get_user_subscription, name='user_subscription'),
    # path('user_membership', views.user_membership, name='user_membership'),
    # path('', views.membership_list, name='membership_list'),

    # Stripe
    path('payment_history/', views.payment_history, name='payment_history'),
    path("config/", views.stripe_config),

    path('create-checkout-session/', CreateCheckoutSession.as_view(), name='create_checkout_session'),
    path("success/", views.success, name='success'),
    path("cancel/", views.cancel, name='cancel'),
    # path("webhook/", views.stripe_webhook, name='stripe_webhook'),
]
