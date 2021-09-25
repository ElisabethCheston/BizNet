from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
# from multiselectfield import MultiSelectField
from itertools import chain
import random


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


class Skills(models.Model):
    skills_name = models.CharField(max_length=200, null=True, blank=False)
    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skills_name


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
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
"""

# Create Profileuser model.
class Profileuser(models.Model):
    """
    Profile user information 
    """
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='profileavatars', default='profileavatar.png')
    picture = models.ImageField(upload_to='images', default='profileavatar.png')
    following = models.ManyToManyField(
        User, related_name='following', blank=True)
    updated = models.DateTimeField(auto_now=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    first_name = models.CharField(
        max_length=254, blank=False, null=True)
    last_name = models.CharField(
        max_length=254, blank=False, null=True)
    title = models.CharField(max_length=254, blank=True, default=None, null=True)
    company_name = models.CharField(
        max_length=254, blank=True, null=True)
    company_number_vat = models.CharField(
        max_length=254, blank=True, default=None, null=True)

    industry = models.ForeignKey(
        Industry, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    profession = models.ForeignKey(
        Profession, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    skill = models.CharField(max_length=254, blank=True, null=True, default=None)
    description = models.TextField(max_length=250, null=True, verbose_name="Description")

    email = models.EmailField(
        max_length=100, null=False, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=False)
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    # city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    
    business = models.ForeignKey(
        Business, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    skills = models.ForeignKey(
        Skills, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    employment = models.ForeignKey( Employment, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    status = models.ForeignKey( Status, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    locations = CountryField(blank_label='Locations', null=True, blank=False)

    def __str__(self):
        # pylint: disable=maybe-no-member
        # return self.user.username
        return str(self.username)

            
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
            p = Profileuser.objects.get(user=u)
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



# FOLLOWING

# People that am following
    def get_following(self):
        # pylint: disable=maybe-no-member
        return self.following.all()

# Following list
    def get_followings_contact(self):
        # pylint: disable=maybe-no-member
        following_list = [p for p in self.get_following()]
        return following_list

# Count of people am following
    @property
    def following_count(self):
        return self.get_following().count()


# FOLLOWERS

# People that are following me
    def get_followers(self):
        # pylint: disable=maybe-no-member
        qs = Profileuser.objects.all()
        followers_list = []
        for profile in qs:
            # if me as a user is on other users following list..
            if self.user in profile.get_following():
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
    def get_proposal_contact(self):
        """
        - Get the profiles
        - Create followers list for login user
        - Loop through list, find contacts we're not connected to.
        - Shuffle the list on every refresh
        - Return 3 available contacts
        """
        # pylint: disable=maybe-no-member
        profiles = Profileuser.objects.all().exclude(user=self.user)
        followers_list = [p for p in self.get_following()]
        available = [p.user for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]

"""
@receiver(post_save, sender=User)
def create_or_update_profileuser(sender, instance, created, **kwargs):
    
    Create or update the profileuser
    
    if created:
        Profileuser.objects.create(user=instance)
    instance.profileuser.save()


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profileuser(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
"""
