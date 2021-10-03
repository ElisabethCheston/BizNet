from django.shortcuts import render
from profileusers.models import Profileuser
from gigs.models import Gig
from django.contrib.auth import get_user_model

from . import views
from django.views.generic import (
    TemplateView, 
    View, 
    ListView,
    DetailView,
)


# Create your views here.

# ALL USERS

class ProfilesListView(ListView):
    model = Profileuser
    template_name = 'network/all_profiles.html'
    context_object_name = 'profileusers'

    # override the queryset method
    def get_queryset(self):
        queryset = Profileuser.objects.order_by('last_name')
        return Profileuser.objects.order_by('last_name').exclude(username=self.request.user)



    

class NetworkProfileView(DetailView):
    model = Profileuser
    template_name = 'network/network_profile_details.html'

    def get_user_profile(self, username):   
        return get_object_or_404(User, pk=username)
     #I know pk=username is not correct. I am not sure what to put pk=?
"""
  # I was able to get the writers other posts using the code below. I did not have to show this code for this question. But just to show you that the pk above has to be username. Or Else the code below won't work(I guess)        
    def get_context_data(self, **kwargs):
        context = super(NetworkProfileView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(user__username__iexact=self.kwargs.get('username'))
        return context  """

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
