from django.shortcuts import render
from .models import Membership
from profileusers.models import Profileuser
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


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

"""
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'https://biz-net.herokuapp.com'
        prices = stripe.Price.list(
            lookup_keys=[request.form['lookup_key']],
            expand=['data.product']
        )
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': prices.data[0].id,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN +
            '/success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(e)
        return "Server error", 500
"""

