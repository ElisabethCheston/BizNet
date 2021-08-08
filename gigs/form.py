from django.contrib.auth.models import User
from django import forms
from .models import Profileuser, Gigs, Industry

from django_countries.fields import CountryField


class GigsForm(forms.ModelForm):
    class Meta:
        model = Profileuser
        fields = [
            'title',
            'author',
            'deadline',
            'created',
            'updated',
            'liked',
            'industry',
            'profession',
            'extrainfo',
            'gigdescription',
            'extrainfo',
            'city',
            'country',
        ]
