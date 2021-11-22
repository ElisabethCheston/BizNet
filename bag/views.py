from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from membership.models import Membership

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, membership_id):
    """ Add a quantity of the specified product to the shopping bag """

    membership = get_object_or_404(Membership, pk=membership_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    request.session['bag'] = bag
    return redirect(redirect_url)
    

def adjust_bag(request, membership_id):
    """Adjust the quantity of the specified membership to the specified amount"""

    membership = get_object_or_404(Membership, pk=membership_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, membership_id):
    """Remove the item from the shopping bag"""

    try:
        membership = get_object_or_404(membership, pk=membership_id)
        bag = request.session.get('bag', {})

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)