from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from membership.models import Membership

def bag_contents(request):

    bag_memberships = []
    total = 0
    membership_count = 0
    bag = request.session.get('bag', {})

    for membership_id, membership_data in bag.memberships():
        if isinstance(membership_data, int):
            membership = get_object_or_404(Membership, pk=membership_id)
            total += membership_data * membership.price
            membership_count += membership_data
            bag_memberships.append({
                'membership_id': membership_id,
                'quantity': membership_data,
                'membership': membership,
            })
        else:
            membership = get_object_or_404(Membership, pk=membership_id)
            for size, quantity in membership_data['memberships_by_size'].memberships():
                total += quantity * membership.price
                membership_count += quantity
                bag_memberships.append({
                    'membership_id': membership_id,
                    'quantity': quantity,
                    'membership': membership,
                    'size': size,
                })
    
    grand_total = delivery + total
    
    context = {
        'bag_memberships': bag_memberships,
        'total': total,
        'membership_count': membership_count,
        'grand_total': grand_total,
    }

    return context