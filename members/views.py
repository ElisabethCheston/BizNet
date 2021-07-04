from django.shortcuts import render
from .models import Member


# Create your views here.
def get_member_profile(request):
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'members/member_profile.html', context)