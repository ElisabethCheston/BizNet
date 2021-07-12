"""
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    avatar = models.ImageField(upload_to='avatars', default='avatar.png')
    # following = models.ManyToManyField(User, related_name='following', blank=True)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=254, null=False, blank=False)


    def __str__(self):
        return str(self.user)
        """