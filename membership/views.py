from django.shortcuts import render
from .models import Membership


# Create your views here.
def get_membership_profile(request):
    membership = Membership.objects.all()
    template = 'membership/member_profile.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)
