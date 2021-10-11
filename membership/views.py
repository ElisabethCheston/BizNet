from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Membership
from profileusers.models import Profileuser
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {"publicKey": settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=True)


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
# Create your views here.
def homepage(request):
  return render(request, "home.html")

@login_required
def checkout(request):
  products = Product.objects.all()
  return render(request,"checkout.html",{"products": products})
"""

# -- Reference : https://github.com/sunilale0/django-stripe-subscription -- #
@csrf_exempt
def create_checkout_session(request):
    if request.method == "GET":
        domain_url = 'https://biz-net.herokuapp.com'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id = request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=domain_url + "cancel/",
                payment_method_types= ["card"],
                mode = "subscription",
                line_items=[{
                    'price': '{{PRICE_ID_1}}',
                    'quantity': 1,
                }, {
                    'price': '{{PRICE_ID_2}}',
                    'quantity': 1,
                }, {
                    'price': '{{PRICE_ID_3}}',
                    'quantity': 1,
                }],
            )
            return JsonResponse({"sessionId": checkout_session["id"]})
        except Exception as e:
            return JsonResponse({"error": str(e)})

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
    # except Exception as e:
        # print(e)
        return "Server error", 500
"""