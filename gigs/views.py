from django.shortcuts import render, redirect, reverse
from .models import Gig, Industry
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from django.core import serializers

# Create views for Gigs


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
    return JsonResponse({'data': data})