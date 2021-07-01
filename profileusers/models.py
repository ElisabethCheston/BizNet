from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.

class Profileuser(models.Model):
    """
    Profile user information 
    """
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True, blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=50)
    company_number_vat = models.CharField(max_length=50, blank=True)
    # industry = models.ForeignKey(
    #     'Industry', null=True, on_delete=models.SET_NULL)
    profession = models.CharField(max_length=50)  
    skill = models.CharField(max_length=254)           
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(default='profile-img.jpg', null=True, blank=True)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=False)

    def __str__(self):
        return self.username


class Industry(models.Model):
    prof_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Industries'

    def __str__(self):
        return self.prof_name
