from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from profileusers.models import Membership



def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {}) # selected_membership_type

    for item_id, item_data in bag.items(): # Fix Items!
        if isinstance(item_data, int):
            product = get_object_or_404(Membership, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
            """
        else:
            product = get_product_or_404(Membership, pk=item_id)
            """

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }
    return context
