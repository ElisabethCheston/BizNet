from django.db import models
from django.contrib.auth.models import User
from profileusers.models import Profileuser, Industry

from django_countries.fields import CountryField


# Create your models here.
class Gig(models.Model):
    title = models.CharField(max_length=50, blank=False)
    picture = models.ImageField(upload_to='images', blank=True)
    industry = models.ForeignKey(
        Industry, null=True, on_delete=models.SET_NULL, blank=True, default=None)
    liked = models.ManyToManyField(User, default=None, blank=False)
    city = models.CharField(max_length=50, null=True,
                            blank=False, default='City')
    country = CountryField(blank_label='Country', null=True, blank=False)
    gigdescription = models.TextField(max_length=250, null=True)
    author = models.ForeignKey(
        Profileuser, on_delete=models.CASCADE, null=True, related_name='gig')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.title)

    def get_liked(self):
        # pylint: disable=maybe-no-member
        return self.liked.all()

    @property
    def like_count(self):
        # pylint: disable=maybe-no-member
        return self.liked.all().count()

    def get_user_liked(self, user):
        pass
