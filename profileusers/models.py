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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='profileavatar.png')
    background = models.ImageField(upload_to='media/images', default='media/images/backgroundpic.jpg')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    # user_id = models.CharField(max_length=254)
    updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    username = models.CharField(max_length=254)
    password = models.CharField(max_length=254, null=True, blank=True)
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    title = models.CharField(max_length=254, blank=True)
    company_name = models.CharField(max_length=254)
    company_number_vat = models.CharField(max_length=254, blank=True)
    # industry = models.ForeignKey(
    #     'Industry', null=True, on_delete=models.SET_NULL, blank=True, default=None)
    profession = models.CharField(max_length=254)  
    skill = models.CharField(max_length=254)           
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(default='profile-img.jpg', null=True, blank=True)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=False)

    def __str__(self):
        return str(self.user)


class Industry(models.Model):
    prof_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Industries'

    def __str__(self):
        return self.prof_name
