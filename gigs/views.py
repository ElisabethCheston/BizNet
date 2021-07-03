from django.shortcuts import render
from .models import Gig

# Create your views here.

def gig(request):
    # gigs = Profileusers.objects.all()
    # context = {
    #    'gigs': gigs
    # }
    return render(request, 'gigs/gig.html')