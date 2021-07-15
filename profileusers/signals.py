from .models import Profileuser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

<<<<<<< HEAD

# Create signal for User to connect with Profileuser
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # pylint: disable=maybe-no-member
=======
"""
@receiver(post_save, sender=User)
def create_profileuser(sender, instance, created, **kwargs):
>>>>>>> 488e657 (Recover project files and update migrations.)
    if created:
        # pylint: disable=maybe-no-member
        Profileuser.objects.create(user=instance)
<<<<<<< HEAD
    # instance.profileuser.save()
=======
    # Existing users: just save the profile
    instance.profile.save()
    """
>>>>>>> 488e657 (Recover project files and update migrations.)
