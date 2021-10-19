from itertools import chain
import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from django.dispatch import receiver

from profileusers.models import Profileuser, Industry, Profession
from gigs.models import Gig



# DROPDOWN LISTS
class Industry(models.Model):
    industry_name = models.CharField(max_length=100, null=True, blank=False)
    class Meta:
        verbose_name_plural = 'Industries'

    def __str__(self):
        return self.industry_name


class Profession(models.Model):
    profession_name = models.CharField(max_length=100, null=True, blank=False)
    class Meta:
        verbose_name_plural = 'Profession'

    def __str__(self):
        return self.profession_name


class Business(models.Model):
    business_name = models.CharField(max_length=200, null=True, blank=False)
    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return self.business_name


class Employment(models.Model):
    employment_name = models.CharField(max_length=200, null=True, blank=False)
    class Meta:
        verbose_name_plural = 'Employment'

    def __str__(self):
        return self.employment_name


class Status(models.Model):
    status_name = models.CharField(max_length=200, null=True, blank=False)
    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status_name

"""
class Notification(models.Model):
    # 1 = Like, 2 = Comment, 3 = Follow
    notification_type = models.IntegerField(null=True, blank=True)
    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    gig = models.ForeignKey('Gig', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    user_has_seen = models.BooleanField(default=False)


# Create NetworkUsers model.
class NetworkUsers(models.Model):

    # Network User Information 

    # Personal information
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images', default='profileavatar.png')
    first_name = models.CharField(
        max_length=254, blank=False, null=True)
    last_name = models.CharField(
        max_length=254, blank=False, null=True)
    email = models.EmailField(
        max_length=100, null=False, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=False)

    # Work Information
    title = models.CharField(max_length=254, blank=True, default=None, null=True)
    company_name = models.CharField(
        max_length=254, blank=True, null=True)
    industry = models.ForeignKey(
        Industry, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    profession = models.ForeignKey(
        Profession, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    description = models.TextField(max_length=250, null=True, verbose_name="Description")
    employment = models.ForeignKey( Employment, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    status = models.ForeignKey( Status, null=True, on_delete=models.SET_NULL, blank=True, default=None)        

    # Other Information
    gig = models.ForeignKey('Gig', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    follow = models.ManyToManyField(
        User, related_name='follow', blank=True)
    updated = models.DateTimeField(auto_now=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)


    def __str__(self):
        # pylint: disable=maybe-no-member
        return str(self.username)
"""

"""
# FOLLOWING

# People that am following
    def get_follow(self):
        # pylint: disable=maybe-no-member
        return self.follow.all()

# Following list
    def get_follows_contact(self):
        # pylint: disable=maybe-no-member
        follow_list = [p for p in self.get_follow()]
        return follow_list

# Count of people am following
    @property
    def follow_count(self):
        return self.get_follow().count()


# FOLLOWERS

# People that are following me
    def get_followers(self):
        # pylint: disable=maybe-no-member
        qs = NetworkUsers.objects.all()
        followers_list = []
        for profile in qs:
            # if me as a user is on other users following list..
            if self.user in profile.get_follow():
                followers_list.append(profile)
            # ...append them too the followers list
        return followers_list

# Count of people that are following me
    @property
    def followers_count(self):
        return len(self.get_followers())


# MATCHING PREFERENCES

# SUGGESTED CONTACTS

# Suggested contacts
    def get_contact_suggestions(self):

        # - Get the profiles
        # - Create followers list for login user
        # - Loop through list, find contacts we're not connected to.
        # - Shuffle the list on every refresh
        # - Return 3 available contacts

        # pylint: disable=maybe-no-member
        profiles = NetworkUsers.objects.all().exclude(user=self.user)
        followers_list = [p for p in self.get_follow()]
        available = [p.user for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]

    
# ALL MY AND MY CONTACTS GIGS

# All my gigs
    def my_gigs(self):
        return self.gig_set.all()

# Number of my posted gigs
    @property
    def num_gigs(self):
        # pylint: disable=maybe-no-member
        return self.gig_set.all().count() 


# All created gigs from contacts I follow 
    def get_contact_gigs(self):
        # pylint: disable=maybe-no-member
        # Loop through the users to get contacts am following...
        users = [user for user in self.get_following()]
        gigs = []
        qs = None
        for u in users:
            # ..then get their profile and the gigs they created..
            p = NetworkUsers.objects.get(user=u)
            p_gigs = p.gig_set.all()
            # ...and append it to the empty gigs list.
            gigs.append(p_gigs)

        # (if I want to include my own in the list)
        # my_gigs = self.gig_set.all()
        # gigs.append(my_gigs) 
        if len(gigs) > 0:
            qs = sorted(chain(*gigs), reverse=True, key=lambda obj: obj.created)
        return qs

    
    class Meta:
        ordering = ('-created',)
"""
