from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
# from .models import User

from .models import Profileuser

# Create your views here.

def profile(request):
    # profiles = Profileusers.objects.all()
    template = 'profileusers/profile.html'
    context = {
       'profiles': profile,
    }
    return render(request, template, context)
