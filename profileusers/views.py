from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import User

from .models import Profileuser, Industry

# Create your views here.

def profile(request):
    """ A view to return the profileusers page """

    context = {
        'profile': profile,
    }

    return render(request, 'profileusers/profile.html', context)
