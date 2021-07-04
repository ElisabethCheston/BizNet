from django.db import models


# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.username
