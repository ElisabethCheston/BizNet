from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Reference: https://www.youtube.com/watch?v=zu2PBUHMEew&t=155s
# Reference : https://medium.com/analytics-vidhya/django-and-stripe-subscriptions-part-2-8ddd406458a9


MEMBERSHIP_CHOICES = (
    ('Yearly', 'yearly'),
    ('Monthly', 'monthly'),
    ('Free', 'free')
)
class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, 
        default='Free', 
        max_length=30)
    price = models.IntegerField(default=15)
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
        

def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)

    user_membership, created = UserMembership.objects.get_or_create(user=instance)

    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        user_membership.stripe_customer_id = new_customer_id['id']
        user_membership.save()

post_save.connect(post_save_usermembership_create, sender=settings.AUTH_USER_MODEL)


# -- Subsciption is only created when a member choose a payment plan -- #

class Subsciption(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
        
