from .models import Profileuser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create signal for User to connect with Profileuser
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # pylint: disable=maybe-no-member
    if created:
        Profileuser.objects.create(user=instance)
    # instance.profileuser.save()
