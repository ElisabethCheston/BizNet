from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
"""
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, get_user_model, update_session_auth_hash)
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm, UserCreationForm
"""
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView, View
from .models import Profileuser

from .forms import ProfileForm, RegisterUserForm, ProfileForm1, ProfileForm2, ProfileForm3


# REGISTRATION & LOGIN

def Register(request):
    # pylint: disable=maybe-no-member
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_register_page')
    else:
        form = RegisterUserForm()

    context = {
        'form' : form
    }
    return render(request, 'profileusers/register.html', context)


def terms(request):
    # pylint: disable=maybe-no-member
    template = 'profileusers/terms.html'

    return render(request, template)


@login_required
def ProfileOne(request):
    profile_form1 = ProfileForm1()
    if request.method == 'POST':
        profile_form1 = ProfileForm1(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profile_form1.is_valid():
            profile_form1.save()
            messages.success(request, 'Step 1 of 3 done of creating your profile!')
            return redirect('register_3')
        # else:
            #messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile = Profileuser.objects.create(user=request.user)
        # profile_form1 = ProfileForm1(instance=request.user.profileuser)
    context = {
        'profile_form1':profile_form1,
        # 'on_profile_page': True
    }
    return render(request, 'profileusers/register_1.html', context)


@login_required
def ProfileTwo(request):
    if request.method == 'POST':
        profile_form2 = ProfileForm2(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profile_form2.is_valid():
            profile_form2.save()
            messages.success(request, 'Step 2 of 3 done of creating your profile!')
            return redirect('register_3')
        else:
            messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile_form2 = ProfileForm2(instance=request.user.profileuser)
    context = {
        'profile_form2':profile_form2,
        # 'on_profile_page': True
    }
    return render(request, 'profileusers/register_2.html', context)


def ProfileThree(request):
    if request.method == 'POST':
        profile_form3 = ProfileForm3(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profile_form3.is_valid():
            profile_form3.save()
            messages.success(request, 'Step 3 of 3 done of creating your profile!')
            return redirect('profile_details')
        else:
            messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile_form3 = ProfileForm3(instance=request.user.profileuser)
    context = {
        'profile_form3' : profile_form3
    }
    return render(request, 'profileusers/register_3.html', context)


"""
@login_required
def RegisterPage(request):
    profile_form = EditForm()
    if request.method == 'POST':
        profile_form = EditForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user # Profileuser.objects.create(user=instance)
            
            profile_form.save()
            # messages.success(request, 'Your Profile has been updated!')
            return redirect('login')
        # else:
            # messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile_form = EditForm()

    context = {
        'profile_form' : profile_form
    }
    return render(request, 'profileusers/register_profile.html', context)
"""

# SINGIN TO ACCOUNT
def loginPage(request):
    if request.method == 'POST':
        # Connected to the name field in the login_page.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_details')

        else:
            messages.info(request, 'Username or Password is incorrect!')
            
    template = 'profileusers/login_page.html'
    context = {}
    return render(request, template, context)


def loginRegisterPage(request):
    if request.method == 'POST':
        # Connected to the name field in the login_page.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register_1')

        else:
            messages.info(request, 'Username or Password is incorrect!')
            
    template = 'profileusers/login_register_page.html'
    context = {}
    return render(request, template, context)


# PROFILES

# @login_required
def profile_details(request):
    # pylint: disable=maybe-no-member
    #profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/profile_details.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile_details')
        else:
            messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        form = ProfileForm(instance=request.user.profileuser)
    context = {
        'form':form,
        # 'on_profile_page': True
    }
    return render(request, 'profileusers/profile_edit.html', context)



@login_required
def all_profiles(request):
    # pylint: disable=maybe-no-member
    profiles = Profileuser.objects.all()
    template = 'profileusers/all_profiles.html'
    context = {
        'profiles': profiles,
    }
    return render(request, template, context)


# MY GIGS

@login_required
def my_gigs(request):
    # pylint: disable=maybe-no-member
    # profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/my_gigs.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def create_gig(request):
    # pylint: disable=maybe-no-member
    #profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/create_gig.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


# CONTACTS

@login_required
def my_contacts(request):
    # pylint: disable=maybe-no-member
    # profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/my_contacts.html'
   
    context = {
        'profile': profile,
        # 'get_following': get_following,
        # 'get_followers': get_followers,
    }
    return render(request, template, context)


# SUGGEST BUTTON OF PPL TO FOLLOW

# class for random contacts to add

class MyProfile(TemplateView):
    template_name = 'profileusers/profile_details.html'


class ProfileData(View):
    def get(self, *args, **kwargs): # , *args, **kwargs
        # pylint: disable=maybe-no-member
        profile = Profileuser.objects.get(user=self.request.user)
        qs = profile.get_proposal_contact()
        profile_to_follow_list = []
        for user in qs:
            # Select random profiles
            p = Profileuser.objects.get(user__username=user.username)
            # p = get_object_or_404(Profileuser, user__username=user.username)
            profile_item = {
                # 'id': p.id,
                'user': p.user.username,
                'firstname': p.firstname,
                'lastname': p.lastname,
                'avatar': p.avatar.url,
                'profession': p.profession,
                'company_name': p.company_name,
            }
            profile_to_follow_list.append(profile_item)
        return JsonResponse({'pf_data': profile_to_follow_list})
