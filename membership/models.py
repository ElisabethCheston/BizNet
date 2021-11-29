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
        default='', 
        max_length=30)
    description = models.TextField(default='')
    description1 = models.TextField(default='')
    description2 = models.TextField(default='')
    description3 = models.TextField(default='')
    description4 = models.TextField(default='')
    price = models.IntegerField(default=15)
    stripe_price_id = models.CharField(
        default='', 
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

post_save.connect(post_save_usermembership_create, sender=settings.AUTH_USER_MODEL)

