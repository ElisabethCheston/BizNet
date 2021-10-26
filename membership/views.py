from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import  ListView

from .models import Membership, UserMembership, Subscription
# Import from other models
from profileusers.models import Profileuser
from gigs.models import Gig

import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

API_KEY = settings.STRIPE_SECRET_KEY
# logger = logging.getLogger(__name__)


                # --  Reference  -- #
"""
https://github.com/sunilale0/django-stripe-subscription
https://stripe.com/docs/billing/integration-builder
"""

# -- STRIPE -- #

@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {"publicKey": settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=True)

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
"""
@require_POST
# login_required
def payment_method(request):
    stripe.api_key = API_KEY
    plan = request.POST.get('plan', 'm')
    automatic = request.POST.get('automatic', 'on')
    payment_method = request.POST.get('payment_method', 'card')
    context = {}

    plan_inst = SubscriptionPlan(plan_id=PRICE_LOOKUP_KEY)

    payment_intent = stripe.PaymentIntent.create(
        amount=plan_inst.amount,
        currency=plan_inst.currency,
        payment_method_types=['card']
    )

    if payment_method == 'card':
        context['secret_key'] = payment_intent.client_secret
        context['STRIPE_PUBLIC_KEY'] = SETTINGS.STRIPE_PUBLIC_KEY
        context['customer_email'] = request.user.email
        context['payment_intent_id'] = payment_intent.id

        return render(request, 'membership/card.html', context)

def profile(request):
    logger.info('profile')
    return render(request, 'my_profile.html')

def card(request):
    return render(request, 'success.html')
"""

# -- SUBSCRIPTION -- #
"""
def subscriptions(request):
    membership = Membership.objects.all()
    template = 'membership/subscriptions.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)
"""

# -- MEMBERSHIP -- #
"""
def membership_list(request):
    membership = Membership.objects.all()
    template = 'membership/membership_list.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)
"""

def get_user_membership(request):
   user_membership_qs = UserMembership.objects.filter(user = request.user)
   if user_membership_qs.exists():
       return user_membership_qs.first()

   return None

def get_user_subscription(request): 
   user_subscription_qs =  Subscription.objects.filter(
       user_membership = get_user_membership(request))
   if user_subscription_qs.exists():
       user_subscription = user_subscription_qs.first()
       return user_subscription
   return None 

def get_selected_membership(request):
   membership_type = request.session['selected_membership_type']   
   selected_membership_qs = Membership.objects.filter(
           membership_type=membership_type)
   if selected_membership_qs.exists():
       return selected_membership_qs.first()
   return None 

class MembershipSelectView(ListView):
   model = Membership
   def get_context_data(self, *args, **kwargs):
       context = super().get_context_data(**kwargs)
       current_membership = get_user_membership(self.request)
       context['current_membership'] = str(current_membership.membership)
       return context

   def post(self, request, **kwargs):
       selected_membership_type = request.POST.get('membership_type')  
       user_membership = get_user_membership(request)
       user_subscription = get_user_subscription(request)      
       selected_membership_qs =Membership.objects.filter(
           membership_type = selected_membership_type) 
       if selected_membership_qs.exists():
           selected_membership = selected_membership_qs.first()

           #validation

       if user_membership.membership == selected_membership:
           if user_subscription != None:
               messages.info(request, "you already have this membership. your \
                   next payment is due {}".format('get this value from stripe'))
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

       request.session['selected_membership_type'] = selected_membership.membership_type       
       return HttpResponseRedirect(reverse('membership_payment'))


def PaymentView(request):
   user_membership = get_user_membership(request)
   selected_membership = get_selected_membership(request)
   publishKey = settings.STRIPE_PUBLIC_KEY

   context = {
       'publishKey': publishKey,
       'selected_membership': selected_membership
   }
   return render(request, "membership/membership_payment.html", context)



"""
def get_user_membership(request, member_pk, *args, **kwargs):
    member_id = UserMembership.objects.filter(pk=member_pk)
    if member_pk.exists():
        membership = member_id.first()

    user_membership = UserMembership.objectsfilter(user=request.user).first()
    user_membership_type = user_membership.membership.membership_type

    context = {
        'member_id': member_id
    }
        
    return render(request, 'user_membership.html', context)
"""


def membership_profile(request):
    membership = Membership.objects.all()
    template = 'membership/membership_profile.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)


# -- PAYMENT HISTORY -- #

def payment_history(request):
    membership = Membership.objects.all()
    template = 'membership/payment_history.html'
    context = {
        'membership': membership
    }
    return render(request, template, context)


# -- CHECKOUT -- #
"""
 def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
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
        mode='payment',
        success_url='membership/templates/membership/membership_success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='membership/templates/membership/membership_cancel',
    )
    return render(request, 'membership_profile,html')

    context = {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
"""
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


# -- SUBSCRIPTION RESPONCES -- #

def success(request):
    template = 'membership/profile_details.html'
    return render(request, template)

def cancel(request):
    template = 'membership/profile_details.html'
    return render(request, template)
