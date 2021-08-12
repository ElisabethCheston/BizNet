from .models import Profileuser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profileuser(sender, instance, created, **kwargs):
    if created:
        # pylint: disable=maybe-no-member
        Profileuser.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()


"""
from django.db.models.signals import post_save, pre_save
from .models import Ext_User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=Ext_User)
def create_profile(sender, instance, created, **kwargs):
   if created:
       profile = Profileuser()
       profile.member_id = str(instance.username) + str(datetime.datetime.now())
       profile.user_id = instance.pk
       profile.save()
"""