from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Gig(models.Model):
    title = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to='images', blank=True)
    gig_description = models.TextField(max_length=250, blank=True)
    liked = models.ManyToManyField(User, default=None, blank=True)
    # author
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    def get_liked(self):
        return self.liked.all()

    @property
    def like_count(self):
        return self.liked.all().count()

    def get_user_liked(self, user):
        pass
