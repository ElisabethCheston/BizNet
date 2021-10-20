from itertools import chain
import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from django.dispatch import receiver

from profileusers.models import Profileuser, Profession, Business, Status, Employment
from membership.models import Membership
from gigs.models import Gig



class Notification(models.Model):
    # 1 = Like, 2 = Comment, 3 = Follow
    notification_type = models.IntegerField(null=True, blank=True)
    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    gig_type = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    user_has_seen = models.BooleanField(default=False)
    allowed_membership = models.ManyToManyField(Membership)

    # Notificatons for different modals
    notice_profession = models.ForeignKey(
        Profession, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    notice_status = models.ForeignKey( Status, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    notice_business = models.ForeignKey(
        Business, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    notice_employment = models.ForeignKey( Employment, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    notice_locations = CountryField(blank_label='notification_locations', null=True, blank=False)
    notice_following = models.ManyToManyField(
        User, related_name='notice_following', blank=True)

    def __str__(self):
        # pylint: disable=maybe-no-member
        return str(self.username)
