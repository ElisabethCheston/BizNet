from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from profileusers.models import Profileuser

# Create your models here.
class Gig(models.Model):
    title = models.CharField(max_length=50, blank=False)
    picture = models.ImageField(upload_to='images', blank=True)
    # user_profile = models.ForeignKey(Profileuser, on_delete=models.SET_NULL, null=True, blank=True)
    gig_description = models.TextField(max_length=250)
    # liked = models.ManyToManyField(User, default=None, blank=False)
    author = models.ForeignKey(Profileuser, on_delete=models.CASCADE, null=True, related_name='gig')
    # updated = models.DateTimeField(auto_now=True)
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
