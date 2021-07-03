from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
# from .models import User
from .models import Gig

# Create your views here.

def gig(request):
    # gigs = Profileusers.objects.all()
    # context = {
    #    'gigs': gigs
    # }
    return render(request, 'gigs/gig.html')
