from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Profileuser

from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView, View


def profile_details(request):
    # pylint: disable=maybe-no-member
    #profile = get_object_or_404(Profileuser, user=request.user)
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
    template_name = 'profileusers/profile_details.html'


class ProfileData(View):
    def get(self, *args, **kwargs): # , *args, **kwargs
        # pylint: disable=maybe-no-member
        profile = Profileuser.objects.get(user=self.request.user)
        qs = profile.get_proposal_contact()
        profile_to_follow_list = []
        for user in qs:
            # Select random profiles
            # p = Profileuser.objects.get(user__username=user.username)
            p = get_object_or_404(Profileuser, user__username=user.username)
            profile_item = {
                # 'id': p.id,
                'user': p.user.username,
                'avatar': p.avatar.url,
            }
            profile_to_follow_list.append(profile_item)
        return JsonResponse({'pf_data': profile_to_follow_list})
