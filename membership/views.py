from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import  ListView, TemplateView
from profileusers.models import Profileuser, Industry, Profession, Employment, Status

from .models import Subscription
from .forms import SubscriptionForm

from gigs.models import Gig
from bag.contexts import bag_contents
from membership.models import Membership


import stripe
import json


stripe.api_key = settings.STRIPE_SECRET_KEY



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
"""
"""

@app.route('/webhook', methods=['POST'])
def webhook_received():
    # Replace this endpoint secret with your endpoint's unique secret
    # If you are testing with the CLI, find the secret by running 'stripe listen'
    # If you are using an endpoint defined with the API or dashboard, look in your webhook settings
    # at https://dashboard.stripe.com/webhooks
    webhook_secret = 'whsec_12345'
    request_data = json.loads(request.data)
    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']
    print('event ' + event_type)
    if event_type == 'checkout.session.completed':
        print('🔔 Payment succeeded!')
    elif event_type == 'customer.subscription.trial_will_end':
        print('Subscription trial will end')
    elif event_type == 'customer.subscription.created':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.updated':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.deleted':
        # handle subscription cancelled automatically based
        # upon your subscription settings. Or if the user cancels it.
        print('Subscription canceled: %s', event.id)
    return jsonify({'status': 'success'})
"""

# -- MEMBERSHIP -- #

def membership_detail(request, membership_id):
    """ A view to show individual membership details """

    membership = get_object_or_404(membership, pk=membership_id)

    context = {
        'membership': membership,
    }

    return render(request, 'memberships/membership_detail.html', context)


"""
def get_user_membership(request):
    user_membership = UserMembership.objects.filter(user = request.user)
    if user_membership.exists():
        return user_membership.first()
    return None


def get_user_subscription(request): 
    user_subscription =  Subscription.objects.filter(
        user_membership = get_user_membership(request))
    if user_subscription.exists():
        user_subscription = user_subscription.first()
        return user_subscription
    return None 


def get_selected_membership(request):
    membership_type = request.session['selected_membership']   
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None
"""
"""
class MembershipSelectView(LoginRequiredMixin, ListView):
    model = Membership

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context.update({
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self, request, **kwargs):
        selected_membership = request.POST.get('membership_type')  
        user_membership = get_user_membership(request)
        # user_subscription = get_user_subscription(request)      
        selected_membership_qs =Membership.objects.filter(
            membership_type = selected_membership) 
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()

           # -- Validation -- #
        if user_membership.membership == selected_membership:
            if user_membership != Free:
                messages.info(request, "You already have this membership.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

<<<<<<< HEAD
        request.session['bag'] = selected_membership.membership_type # selected_membership_type

=======
        request.session['selected_membership'] = selected_membership.membership_type       
>>>>>>> 0ad3775 (Setup Admin membership view.)
        return HttpResponseRedirect(reverse('payment'))
        """

def all_products(request):
    # A view to show all products, including sorting and search queries

    products = Membership.objects.all()
    query = None

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'membership/membership_list.html', context)


def product_detail(request, product_id):
    # A view to show individual product details

    product = get_object_or_404(Membership, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'membership/membership_detail.html', context)


@login_required
def add_product(request):
    # Add a product to the store
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'membership/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    # Edit a product in the store
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Membership, pk=product_id)
    if request.method == 'POST':
        form = SubscriptionFormForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = SubscriptionFormForm(instance=product)
        messages.info(request, f'You are editing {product.membership_type}')

    template = 'membership/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # Delete a product from the store
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('select'))

    product = get_object_or_404(Membership, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))



@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

@login_required
def PaymentView(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }

        order_form = SubscriptionForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Membership.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )

                except Membership.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('select'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = Subscription.objects.get(user=request.user)
                order_form = SubscriptionForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
            except Subscription.DoesNotExist:
                order_form = SubscriptionForm()
        else:
            order_form = SubscriptionForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'membership/membership_payment.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

"""
@login_required
def PaymentView(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    user_membership = get_user_membership(request)

    if request.method == 'POST':
        bag = request.session.get('bag', {})
    try:
        selected_membership = get_selected_membership(request)
    except:
        return redirect(reverse("select"))
    publishKey = settings.STRIPE_PUBLIC_KEY

    if request.method == "POST":
        try:
            token = request.POST['stripeToken']

            # The source for the customer

            customer = stripe.Customer.retrieve(user_membership.stripe_customer_id)
            customer.source = token # 4242424242424242
            customer.save()

            # Create the subscription using only the customer as we don't need to pass their
            # credit card source anymore

            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    { 
                        "price": selected_membership.stripe_price_id,
                        'quantity': 1, 
                        },
                ]
            )

            # return redirect(reverse('update-transactions', kwargs={
                                        # 'subscription_id': subscription.id}))

        except:
            messages.info(request, "An error has occurred, investigate it in the console")

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'selected_membership': selected_membership
    }
    return render(request, "membership/membership_payment.html", context)
"""
"""
class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            stripe_price_id = self.kwargs["pk"]
            membership = Membership.objects.get(id=stripe_price_id)
            intent = stripe.PaymentIntent.create(
                amount=price.price,
                currency='eur',
                customer=customer['id'],
                metadata={
                    "stripe_price_id": membership.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
"""

@login_required
def updateTransactionRecords(request):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    user_membership.membership = selected_membership
    user_membership.save()

    sub, created = Subscription.objects.get_or_create(
        user_membership=user_membership)
    sub.stripe_subscription_id = subscription_id
    sub.active = True
    sub.save()

    try:
        del request.session['selected_membership']
    except:
        pass
        
    messages.info(request, 'Successfully created {} membership'.format(
        selected_membership))
    return redirect(reverse('select'))

"""
# -- WEBHOOK -- #


# -- PROFILEUSER INFO -- #

@login_required
def cancelSubscription(request):
    user_sub = get_user_subscription(request)

    if user_sub.active is False:
        messages.info(request, "You dont have an active membership")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    sub = stripe.Subscription.retrieve(user_sub.stripe_subscription_id)
    sub.delete()

    user_sub.active = False
    user_sub.save()

    free_membership = Membership.objects.get(membership_type='Free')
    user_membership = get_user_membership(request)
    user_membership.membership = free_membership
    user_membership.save()

    messages.info(
        request, "Successfully cancelled membership. We have sent an email")
    # sending an email here

    return redirect(reverse('memberships:select'))

"""
def membership_profile(request):
    user_membership = get_user_membership(request)
    # selected_membership = get_selected_membership(request)
    template = 'membership/membership_profile.html'
    context = {
        'user_membership': user_membership,
        # 'selected_membership': selected_membership,
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



# -- SUBSCRIPTION RESPONCES -- #

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"


# -- ADMIN   -- #
"""
@login_required
def add_membership(request):
    # Add a membership to the store
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('network'))

    if request.method == 'POST':
        form = MembershipForm(request.POST, request.FILES)
        if form.is_valid():
            membership = form.save()
            messages.success(request, 'Successfully added membership!')
            return redirect(reverse('membership_detail', args=[membership.id]))
        else:
            messages.error(request, 'Failed to add membership. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'membership/add_membership.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_membership(request, membership_id):
    # Edit a membership in the store
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('network'))

    membership = get_object_or_404(Membership, pk=membership_id)
    if request.method == 'POST':
        form = MembershipForm(request.POST, request.FILES, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated membership!')
            return redirect(reverse('membership_detail', args=[membership.id]))
        else:
            messages.error(request, 'Failed to update membership. Please ensure the form is valid.')
    else:
        form = MembershipForm(instance=membership)
        messages.info(request, f'You are editing {membership.name}')

    template = 'membership/edit_membership.html'
    context = {
        'form': form,
        'membership': membership,
    }

    return render(request, template, context)


@login_required
def delete_membership(request, membership_id):
    # Delete a membership from the store
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    membership = get_object_or_404(Membership, pk=membership_id)
    membership.delete()
    messages.success(request, 'Membership deleted!')
    return redirect(reverse('membership_list'))
"""