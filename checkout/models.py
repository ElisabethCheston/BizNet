import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from membership.models import Membership, UserMembership


# -- Subscription is only created when a member choose a payment plan -- #
class Subscription(models.Model):
    user_profile = models.ForeignKey(UserMembership, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='subscription')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(
        max_length=254, blank=False, null=True)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=False, default='')
    stripe_customer_id = models.CharField(max_length=40, default='')
    email = models.EmailField(
        max_length=100, null=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):

        # Generate a random, unique order number using UUID

        return uuid.uuid4().hex.upper()

    def update_total(self):

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):

        # Override the original save method to set the order number

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class SubscriptionLineItem(models.Model):
    order = models.ForeignKey(Subscription, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Membership, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        # Override the original save method to set the lineitem total

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SLUG {self.product.slug} on order {self.order.order_number}'