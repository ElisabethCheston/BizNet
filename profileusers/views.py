from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

"""
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, get_user_model, update_session_auth_hash)
from django.contrib.auth.decorators import login_required

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponseRedirect, QueryDict
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
"""

from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView, View
from .models import Profileuser
from .forms import ProfileuserForm, RegisterForm, RegisterUserForm



def Register(request):
    # pylint: disable=maybe-no-member
    form = RegisterUserForm()
    template = 'profileusers/register.html'
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, template, context)
"""
class RegisterPage(View):
    template = 'profileusers/register_profile.html'
    def get_success_url(self):        
        url = self.get_redirect_url()
        if url:
            return reverse("profile_edit")
"""
def loginPage(request):
    if request.method == 'POST':
        # Connected to the name field in the login_page.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my_profile')
    template = 'profileusers/login.html'
    context = {}
    return render(request, template, context)



@login_required
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
        form = ProfileuserForm(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile_details')
        else:
            messages.error(request, 'Update failed. Kindly check\
                that your inputs are valid.')
    else:
        form = ProfileuserForm(instance=request.user.profileuser)
    context = {
        'form':form,
        'on_profile_page': True
    }
    return render(request, 'profileusers/profile_edit.html', context)



# MY GIGS

def my_gigs(request):
    # pylint: disable=maybe-no-member
    # profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/my_gigs.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)

def create_gig(request):
    # pylint: disable=maybe-no-member
    #profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/create_gig.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


# PROFILES

def all_profiles(request):
    # pylint: disable=maybe-no-member
    profiles = Profileuser.objects.all()
    template = 'profileusers/all_profiles.html'
    context = {
        'profiles': profiles,
    }
    return render(request, template, context)


def my_profile(request):
    # pylint: disable=maybe-no-member
    profiles = Profileuser.objects.all()
    template = 'profileusers/my_profile.html'
    context = {
        'profiles': profiles,
    }
    return render(request, template, context)


# CONTACTS

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
"""
class for random contacts to add
"""
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
