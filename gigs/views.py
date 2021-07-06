from django.shortcuts import render
from .models import Gig

# Create your views here.

def gig(request):
    qs = Gig.objects.all()
    context = {
        'hello': 'hello world',
        'qs':qs,
    }
    return render(request, 'gigs/gig.html', context)