from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.


class Industry(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Profileuser(models.Model):
    """
    Membership, network and profile user information 
    """
    industry = models.ForeignKey(
        'Industry', null=True, blank=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    skill = models.CharField(max_length=254)
    profession = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name     

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the users profile
    """
    if created:
        Profileuser.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profileuser.save()
          