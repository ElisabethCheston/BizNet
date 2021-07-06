from django.shortcuts import render
from .models import Gig
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def gig(request):
    qs = Gig.objects.all()
    context = {
        'greeting': 'Welcome!',
        'qs': qs,
    }
    return render(request, 'gigs/gig.html', context)

def gig_json(request):
    qs = Gig.objects.all()
    data = serializers.serialize('json', qs)
    return JsonResponse({'data':data})