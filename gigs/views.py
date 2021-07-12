from django.shortcuts import render
from .models import Gig
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def gig(request):
    # pylint: disable=maybe-no-member
    qs = Gig.objects.all()
    template = 'gigs/gig.html'
    context = {
        'greeting': 'Welcome!',
        'qs': qs,
    }
    return render(request, template, context)

def gig_json(request):
    # pylint: disable=maybe-no-member
    qs = Gig.objects.all()
    data = serializers.serialize('json', qs)
    return JsonResponse({'data':data})
