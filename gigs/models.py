from django.db import models

# Create your models here.

class Gig(models.Model):
    gig = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.gig