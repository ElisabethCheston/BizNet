from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Profileuser

from django.http import JsonResponse
from django.core import serializers
# from .forms import ProfileuserForm


# Create your views here.
def profile_view(request):
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/profile.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


"""
def profile(request): 
    profile = get_object_or_404(Profileuser, user=request.user)
   # form = ProfileuserForm(instance=profile)
    template = 'profileusers/profile.html'
    context = {
        'profiles': profile,
        'on_profile_page': True
    }
    return render(request, template, context)
"""


def all_profiles(request):
    # pylint: disable=maybe-no-member
    profiles = Profileuser.objects.all()
    template = 'profileusers/all_profiles.html'
    context = {
        'profiles': profiles,
    }
    return render(request, template, context)


def profile_details(request):

    profile = get_object_or_404(Profileuser, user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'profileusers/profile_details.html', context)
