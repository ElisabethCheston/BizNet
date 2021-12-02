from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import SubscriptionForm
from .models import Subscription, SubscriptionLineItem

from profileusers.models import Membership, Profileuser
# from membership.forms import UserMembershipForm
from bag.contexts import bag_contents

import stripe
import json



"""
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
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

    order_form = SubscriptionForm()
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
"""


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



def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('select'))

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
                        order_line_item = SubscriptionLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = SubscriptionLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()

                except Profileuser.DoesNotExist:
                    messages.error(request, (
                        "Membership don't seem to exist in our database. "
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
                profile = Profileuser.objects.get(username=request.user)
                order_form = SubscriptionForm(initial={
                    'full_name': profile.username.get_full_name(),
                    'email': profile.username.email,
                })
            except Profileuser.DoesNotExist:
                order_form = SubscriptionForm()
        else:
            order_form = SubscriptionForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    order_form = SubscriptionForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)



def checkout_success(request, order_number):

    # Handle successful checkouts
    save_info = request.session.get('save_info')
    order = get_object_or_404(Subscription, order_number=order_number)

    if request.user.is_authenticated:
        profile = Profileuser.objects.get(username=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        """
        if save_info:
            usermembership_form = UserMembershipForm(membership_type, instance=profile)
            if usermembership_form.is_valid():
                usermembership_form.save()
        """

    messages.success(request, f'Subscription payment successfully processed! \
        Your subscription number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

