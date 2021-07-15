from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Profileuser

from django.http import JsonResponse
from django.core import serializers
# from .forms import ProfileuserForm


# Create your views here.


def all_profiles(request):
    # pylint: disable=maybe-no-member
    profiles = Profileuser.objects.all()
    template = 'profileusers/all_profiles.html'
    context = {
        'profiles': profiles,
    }
    return render(request, template, context)


def profile_details(request):
    """ A view to show individual profile details """

    profile = get_object_or_404(Profileuser, user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'profileusers/profile_details.html', context)
