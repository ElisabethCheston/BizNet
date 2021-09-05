from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    MyProfile,
    ProfileData,
    # RegisterPage,
)


urlpatterns = [
    path('', views.all_profiles, name='profiles'),
    path('my_profile/', MyProfile.as_view(), name='my_profile'), # .as_view() to "convert" a class-based view for url
    path('profile_data/', ProfileData.as_view(), name='profile_data'), # .as_view() to "convert" a class-based view for url
    path('profile_details/', views.profile_details, name='profile_details'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('create_gig/', views.create_gig, name='create_gig'),

    path('register/', views.Register, name='register'),
    # path('register_profile/', views.RegisterPage, name='register_profile'),
    path('profile/', views.Profile, name='profile'),
    path('register_1/', views.ProfileOne, name='register_1'),
    path('register_2/', views.ProfileTwo, name='register_2'),
    path('register_3/', views.ProfileThree, name='register_3'),

    path('login_page/', views.loginPage, name='login_page'),
    path('login_register_page/', views.loginRegisterPage, name='login_register_page'),
    path('terms/', views.terms, name='terms'),
    path('my_gigs/', views.my_gigs, name='my_gigs'),
    path('my_contacts/', views.my_contacts, name='my_contacts'),

    # path('verified_email_required/', auth_views.VerifiedEmailRequiredView.as_view(template_name='verified_email_required.html'), name='verified_email_required'),
    # path('verification_sent/', auth_views.VerdificationSentView.as_view(template_name='verification_sent.html'), name='verification_sent'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
