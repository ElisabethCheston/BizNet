from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Profileuser

from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView, View
from .models import Profileuser
from .forms import ProfileuserForm


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
    usergigs = Profileuser.objects.get(user=request.user)
    template = 'profileusers/my_gigs.html'
    context = {
        'usergigs': usergigs,
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
            # p = Profileuser.objects.get(user__username=user.username)
            p = get_object_or_404(Profileuser, user__username=user.username)
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
