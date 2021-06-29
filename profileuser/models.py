from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.


class Profileuser(models.Model):
    """
    Membership, network and profile user information 
    """
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=254, null=True, blank=True)
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    title = models.CharField(max_length=254, blank=True)

    company_name = models.CharField(max_length=254)
    company_number_vat = models.CharField(max_length=254, blank=True)
    industry = models.ForeignKey(
        'Industry', null=True, on_delete=models.SET_NULL)
    profession = models.CharField(max_length=254)  
    skill = models.CharField(max_length=254)           
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(default='profile-img.jpg', null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=False)
   

    def __str__(self):
        return self.user.username

class Industry(models.Model):

    class Meta:
        verbose_name_plural = 'Industries'

    _id_prof = models.CharField(max_length=254)
    prof_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self._id_prof

    def get_prof_name(self):
        return self.prof_name
