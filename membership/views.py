from django.shortcuts import render
from .models import Membership
from profileusers.models import Profileuser


# Create your views here.
def membership_profile(request):
    membership = Membership.objects.all()
    template = 'membership/membership_profile.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)


def subscriptions(request):
    membership = Membership.objects.all()
    template = 'membership/subscriptions.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)


def my_subscription(request):
    membership = Membership.objects.all()
    template = 'membership/my_subscription.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)


def payment_histrory(request):
    membership = Membership.objects.all()
    template = 'membership/payment_histrory.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)