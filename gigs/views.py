from django.shortcuts import render, redirect, reverse
from .models import Gig, Industry
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from django.core import serializers

# Create your views here.


def gig(request):
    # pylint: disable=maybe-no-member
    qs = Gig.objects.all()
    template = 'gigs/gig.html'

    """
    sort = None
    industry = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                industry = industry.annotate(lower_name=Lower('name'))
            if sortkey == 'industry':
                sortkey = 'industry__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            industry = industry.order_by(sortkey)

        if 'industry' in request.GET:
            categories = request.GET['industry'].split(',')
            industry = industry.filter(industry__name__in=categories)
            categories = Industry.objects.filter(name__in=industry)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('industry'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            industry = industry.filter(queries)

    current_sorting = f'{sort}_{direction}'

    if request.GET:
        if 'industry' in request.GET:
            industry = request.GET['industry'].split(',')
            """
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
