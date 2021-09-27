from .models import Gig
from profileusers.models import Profileuser
from .forms import GigForm

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from django.core import serializers
from django.views.decorators.http import require_http_methods

from django.views.generic import (
    TemplateView, 
    View, 
    DetailView, 
    CreateView, 
    ListView,
    UpdateView,
    DeleteView,
)


"""
def gig(request):
    # pylint: disable=maybe-no-member
    template = 'gigs/gig.html'
    context = {
        # 'greeting': 'Welcome!',
        'qs': Gig.objects.all()
    }
    return render(request, template, context)
"""

# ALL GIGS

class GigListView(ListView):
    model = Gig
    template_name = 'gigs/gig.html'
    context_object_name = 'gigs'
    ordering = ['-created']

class GigDetailView(DetailView):
    model = Gig


# PROFILEUSER GIGS

def my_gigs(request):
    # pylint: disable=maybe-no-member
    profile = Profileuser.objects.get(username=request.user)
    template = 'gigs/my_gigs.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)

"""
def NewGig(request):
    # pylint: disable=maybe-no-member
    new_gig = get_object_or_404(Gig)
    #new_gig = Gig.objects.all()
    context = {
        'new_gig': new_gig,
    }
    return render(request, 'gigs/new_gig.html', context)
"""

class GigCreateView(CreateView, LoginRequiredMixin):
    model = Gig
    form_class = GigForm
    template_name = 'gigs/create_gig.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profileuser
        return super().form_valid(form)


class GigUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gig
    form_class = GigForm
    template_name = 'gigs/create_gig.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profileuser
        return super().form_valid(form)

    def test_func(self):
        gig = self.get_object()
        if self.request.user == gig.author:
            return True
        return False
    

class GigDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gig

    def test_func(self):
            gig = self.get_object()
            if self.request.user == gig.author:
                return True
            return False


# CHOICE FOR GIGS

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


def gig_json(request):
    # pylint: disable=maybe-no-member
    qs = Gig.objects.all()
    data = serializers.serialize('json', qs)
    context = {
        'data': data,
    }
    return JsonResponse(context)
