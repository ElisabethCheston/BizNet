from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    stripe_customer_id = models.CharField(max_length=50)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserMembership.objects.create(user=instance)
    # Existing users: just save the profile
    instance.usermembership.save()