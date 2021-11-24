from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

import stripe

# Reference: https://www.youtube.com/watch?v=zu2PBUHMEew&t=155s
# Reference : https://medium.com/analytics-vidhya/django-and-stripe-subscriptions-part-2-8ddd406458a9

class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(
        default='Free', 
        max_length=30)
    description = models.TextField(default='')
    description1 = models.TextField(default='')
    description2 = models.TextField(default='')
    description3 = models.TextField(default='')
    description4 = models.TextField(default='')
    price = models.IntegerField(default=15)
    stripe_price_id = models.CharField(
        default='PRICE_ID_1', 
        max_length=50)
    

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user.username
    
    @property
    def is_active(self):
        return self.status == "active" or self.status == "trialing"
        

def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    user, created = UserMembership.objects.get_or_create(
        user=instance)

    if user.stripe_customer_id is None or user.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        free_membership = Membership.objects.get(membership_type='Free')
        user.stripe_customer_id = new_customer_id['id']
        user.membership = free_membership
        user.save()
"""
post_save.connect(post_save_usermembership_create, sender=settings.AUTH_USER_MODEL)
"""

# -- Subscription is only created when a member choose a payment plan -- #
class Subscription(models.Model):
    user_profile = models.ForeignKey(UserMembership, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(
        max_length=254, blank=False, null=True)
    last_name = models.CharField(
        max_length=254, blank=False, null=True)
    membership = models.ManyToManyField(Membership)
    stripe_customer_id = models.CharField(max_length=40, default='')
    email = models.EmailField(
        max_length=100, null=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):

        # Generate a random, unique order number using UUID

        return uuid.uuid4().hex.upper()

    def update_total(self):

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):

        # Override the original save method to set the order number

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Subscription, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Membership, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        # Override the original save method to set the lineitem total

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Premium {self.product.PRICE_ID_2} on order {self.order.order_number}'
