from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Profileuser

from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView, View
from django.http import JsonResponse


def profile_details(request):
    # pylint: disable=maybe-no-member
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/profile_details.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


def all_profiles(request):
    # pylint: disable=maybe-no-member
    profiles = Profileuser.objects.all()
    template = 'profileusers/all_profiles.html'
    context = {
        'profiles': profiles,
    }
    return render(request, template, context)

"""
class for random contacts to add
"""
class MyProfile(TemplateView):
    template_name = 'profileusers/my_profile.html'


class ProfileData(View):
    def get(self, *args, **kwargs):
        # pylint: disable=maybe-no-member
        profile = Profileuser.objects.get(user=self.request.user)
        qs = profile.get_proposal_contact()
        to_follow_list = []
        for user in qs:
            p = Profileuser.objects.get(user__username=user.username)
            profile_item = {
                'id': p.id,
                'user': p.user.username,
                'avatar': p.avatar.url,
            }
            to_follow_list.append(profile_item)
        return JsonResponse({'pf_data': to_follow_list})
