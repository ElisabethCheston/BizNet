from django.shortcuts import render
from profileusers.models import Profileuser
from gigs.models import Gig
from django.contrib.auth import get_user_model

from . import views
from django.views.generic import (
    TemplateView, 
    View, 
    ListView,
)


# Create your views here.

# ALL GIGS

class ProfilesListView(ListView):
    model = Profileuser
    template_name = 'network/all_profiles.html'
    context_object_name = 'profileusers'
    ordering = ['-created']

    # override the queryset method
    def get_queryset(self):
        return Profileuser.objects.all().exclude(username=self.request.user)

"""
# @login_required
def all_profiles(request):
    # pylint: disable=maybe-no-member
    all_profiles = Profileuser.objects.all()
    print(all_profiles)
    # print(all_profiles[0]['username'])
    template = 'network/network.html'
    context = {
        'all_profiles': all_profiles,
    }
    return render(request, template, context)


class UserDetailView(DetailView):
    model = Profileuser


def network(request):
    # A view to return the network page 

    return render(request, 'network/network.html')
"""

def myContacts(request):
    """ A view to return the My Contacts page """

    return render(request, 'network/contacts.html')


def my_followers(request):
    """ A view to return the My Contacts page """

    return render(request, 'network/my_followers.html')




# @login_required
def following_ppl(request):
    """ A view to return the My Contacts page """
    # pylint: disable=maybe-no-member
    profile = Profileuser.objects.get(username=request.user)
    template = 'profileusers/my_followers.html'
   
    context = {
        'profile': profile,
        # 'get_following': get_following,
        # 'get_followers': get_followers,
    }
    return render(request, template, context)
