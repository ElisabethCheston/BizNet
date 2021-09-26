from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Gig
from profileusers.models import Profileuser

from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from django.core import serializers

from django.views.generic import TemplateView, View, DetailView, CreateView, ListView
# from .forms import GigForm
from django.views.decorators.http import require_http_methods



def gig(request):
    # pylint: disable=maybe-no-member
    template = 'gigs/gig.html'
    context = {
        # 'greeting': 'Welcome!',
        'qs': Gig.objects.all()
    }
    return render(request, template, context)


class GigListView(ListView):
    model = Gig
    template_name = 'gigs/gig.html'
    context_object_name = 'gigs'
    ordering = ['-created']

class GigDetailView(DetailView):
    model = Gig


def gig_json(request):
    # pylint: disable=maybe-no-member
    qs = Gig.objects.all()
    data = serializers.serialize('json', qs)
    context = {
        'data': data,
    }
    return JsonResponse(context)

# PROFILEUSER GIGS

# @login_required
def my_gigs(request):
    # pylint: disable=maybe-no-member
    profile = Profileuser.objects.get(username=request.user)
    template = 'gigs/my_gigs.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


# @login_required
class GigCreateView(CreateView):
    model = Gig
    template_name = 'gigs/create_gig.html'
    fields = ('title', 'industry', 'profession', 'city', 'country', 'gigdescription', 'extrainfo', 'deadline',)



"""
def AppliedGig(request):
    # pylint: disable=maybe-no-member
    apply_gig = Gig.objects.all()
    # template = 'gigs/apply_gig.html'
    
    return render(request, 'gigs/apply_gig.html')


def HideGig(request):
    # pylint: disable=maybe-no-member
    hide_gig = Gig.objects.all()
    # template = 'gigs/hide_gig.html'
    
    return render(request, 'gigs/hide_gig.html')

"""
def NewGig(request):
    # pylint: disable=maybe-no-member
    new_gig = get_object_or_404(Gig)
    #new_gig = Gig.objects.all()
    context = {
        'new_gig': new_gig,
    }
    return render(request, 'gigs/new_gig.html', context)



def SavedGig(request):
    # pylint: disable=maybe-no-member
    save_gig = Gig.objects.all()
    context = {
        'save_gig': save_gig,
    }
    return render(request, 'gigs/saved_gig.html', context)



def AppliedGig(request):
    # pylint: disable=maybe-no-member
    apply_gig = Gig.objects.all()
    context = {
        'apply_gig': apply_gig,
    }
    return render(request, 'gigs/apply_gig.html', context)


def HideGig(request):
    # pylint: disable=maybe-no-member
    hide_gig = Gig.objects.all()
    context = {
        'hide_gig': hide_gig,
    }
    return render(request, 'gigs/hide_gig.html', context)


"""
@require_http_methods(['POST'])
def HideGig(request):
    # pylint: disable=maybe-no-member
    gd_list = request.POST.get('gd_list')
    noshow = get_object_or_404(Gig, noshowgig=gd_list)
    if noshow:
        an_gig = True
    else:
        an_gig = False
    data = {
        'an_gig': an_gig
    }
    return JsonResponse(data)
"""

class GigsData(View):
    def get(self, *args, **kwargs):
        # pylint: disable=maybe-no-member
        add_gig = Gig.objects.get(user=self.request.user)
        qs = add_gig.get_proposal_contact()
        gd_list = []
        for user in qs:
            # Select random profiles
            # p = Gig.objects.get(user__username=user.username)
            p = get_object_or_404(Gig, user__username=user.username)
            gig_item = {
                # 'id': p.id,
                'author': p.user.username,
                'title': p.user.username,
                'firstname': p.firstname,
                'lastname': p.lastname,
                'avatar': p.avatar.url,
                'profession': p.profession,
                'company_name': p.company_name,
                'industry': p.obj.industry,
                'liked': p.obj.liked,
                'gigdescription': p.obj.gigdescription,
                'extrainfo': p.obj.extrainfo,
                'deadline': p.obj.deadline,
                'updated': p.obj.updated,
                'created': p.obj.created,
                'city': p.obj.city,
                'country': p.obj.country,
            }
            gd_list.append(gig_item)
        return JsonResponse({'pf_data': gd_list})