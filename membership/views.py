from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import  ListView

from .models import Membership, UserMembership, Subsciption
# Import from other models
from profileusers.models import Profileuser
from gigs.models import Gig, NetworkUsers

import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {"publicKey": settings.STRIPE_PUBLIC_KEY}
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


def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    template = 'membership/user_membership.html'

    return render(request, template)


def get_user_subscription(request):
    user_subscription = Subscription.objects.filter(
        user_membership=user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_membership_qs.first()
        return user_subscription

    template = 'membership/user_subscription.html'

    return render(request, template)


class MembershipSelectView(ListView):
    model = Membership

    def get_contex_data (self, *args, **kwargs):
        context = super().get_contex_data(**kwargs)
        current_membership = get_user_membership(self.membership)
        return context

    def post(self, request, **kwargs):
        selected_membership = request.POST.get('membership_type')

        user_membership = get_user_membership(request)
        user_subscription = get_user_subscription(request)

        selected_membership_qs = Membership.objects.filter(
            membership_type=selected_membership_type
        )
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()

    # -- Valitation -- #
"""
    if user_membership.membership == selected_membership:
        if user_subscription != None:
            messages.info(request, "You already have this membership. Your \
                next payment is due {}".format('get this value from stripe'))
            return HttpResponseRedirect(request.META.get(HTTP_REFERER))

    # assign to the session
    request.session['selected_membership_type'] = selected_membership.membership_type
    return HttpResponseRedirect(reverse('memberships:payment'))
"""


# -- PAYMENT HISTORY -- #
def payment_histrory(request):
    membership = Membership.objects.all()
    template = 'membership/payment_histrory.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)

# -- SUBSCRIPTION RESPONCES -- #
def memership_success(request):
    template = 'membership/profile_details.html'
    return render(request, template)

def memership_cancel(request):
    template = 'membership/profile_details.html'
    return render(request, template)


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
            # -- https://stripe.com/docs/billing/integration-builder -- #
"""
# @app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
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
            success_url='https://biz-net.herokuapp.com/' +
            '/success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(e)
        return "Server error", 500
"""
"""
@csrf_exempt
def create_checkout_session(request):
    if request.method == "GET":
        domain_url = 'https://biz-net.herokuapp.com/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            prices = stripe.Price.list(
            lookup_keys=[request.form['lookup_key']],
            expand=['data.product']
        )
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
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

# Stripe Webhook
"""
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get("subscription")

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id = client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        print(user.username + " just subscrbed.")

    return HttpResponse(status=200)
"""