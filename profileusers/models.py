from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


<<<<<<< HEAD
=======

class Industry(models.Model):
    industry_name = models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Industries'


    def __str__(self):
        return self.industry_name


>>>>>>> 488e657 (Recover project files and update migrations.)
# Create Profileuser model.
class Profileuser(models.Model):
    """
    Profile user information 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    avatar = models.ImageField(upload_to='profileavatars', default='profileavatar.png')
    background = models.ImageField(upload_to='backgroundpics', default='backgroundpic.jpg')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    # member_id = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # username = models.CharField(max_length=254)
    # password = models.CharField(max_length=254, null=True, blank=True)
    # firstname = models.CharField(max_length=254)
    # lastname = models.CharField(max_length=254)
    # title = models.CharField(max_length=254, blank=True)
    # company_name = models.CharField(max_length=254)
    # company_number_vat = models.CharField(max_length=254, blank=True)
    # industry = models.ForeignKey(
        # 'Industry', null=True, on_delete=models.SET_NULL, blank=True, default=None)
    # profession = models.CharField(max_length=254)  
    # skill = models.CharField(max_length=254)           
    
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    # image = models.ImageField(default='profile-img.jpg', null=True, blank=True)
    # email = models.EmailField(max_length=50, null=False, blank=False)
    # phone = models.CharField(max_length=20, null=True, blank=True)
    # city = models.CharField(max_length=40, null=True, blank=False)
    # country = CountryField(blank_label='Country', null=True, blank=False)
=======
    avatar = models.ImageField(
        upload_to='profileavatars', default='profileavatar.png')
    background = models.ImageField(
        upload_to='backgroundpics', default='backgroundpic.jpg')
    following = models.ManyToManyField(
        User, related_name='following', blank=True)
    member_id = models.CharField(max_length=254, primary_key=True, default='member_id')
    description = models.TextField(blank=True, default='Bio')
    updated = models.DateTimeField(auto_now=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    firstname = models.CharField(
        max_length=254, blank=False, default='First Name')
    lastname = models.CharField(
        max_length=254, blank=False, default='Last Name')
    title = models.CharField(max_length=254, blank=True, default=None)
    company_name = models.CharField(
        max_length=254, blank=True, default='Company Name')
    company_number_vat = models.CharField(
        max_length=254, blank=True, default=None)
    industry = models.ForeignKey(
        Industry, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    description = models.TextField(max_length=250, null=True)
    profession = models.CharField(
        max_length=254, blank=False, default='Profession')
    skill = models.CharField(max_length=254, blank=True, default=None)
    email = models.EmailField(
        max_length=100, null=False, blank=True, default='Email')
    phone = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=50, null=True,
                            blank=False, default='City')
    country = CountryField(blank_label='Country', null=True, blank=False)
>>>>>>> 488e657 (Recover project files and update migrations.)

    def __str__(self):
        # pylint: disable=maybe-no-member
        # return self.user.username
        return str(self.user)

"""
@receiver(post_save, sender=User)
def create_profileuser(sender, instance, created, **kwargs):

    if created:
        Profileuser.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()


def get_my_gigs(self):
    # pylint: disable=maybe-no-member
    return self.post_set.all()


@property
def num_gigs(self):
    # pylint: disable=maybe-no-member
    return self.profile.poster.all().count()


def get_my_gigs(self):
    # pylint: disable=maybe-no-member
    return self.post_set.all()

<<<<<<< HEAD
class Meta:
    verbose_name_plural = 'Industries'

def __str__(self):
    return self.prof_name
"""
=======
@property
def num_gigs(self):
    # pylint: disable=maybe-no-member
    return self.profile.poster.all().count()

>>>>>>> 488e657 (Recover project files and update migrations.)
