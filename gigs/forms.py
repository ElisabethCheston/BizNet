"""
from django.contrib.auth.models import User
from django import forms
from .models import Gig, Profileuser, Industry, Profession


class GigForm(forms.ModelForm):

    class Meta:
        model = Gig
        field = [
            '__all__',
        ]

    industry = forms.ModelChoiceField(queryset=Industry.objects.all(), empty_label='Industry:')
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label='Profession:')

    class Meta:
        model = Gig
        field = [
            'title',
            'industry',
            'profession',
            'city',
            'country',
            'gigdescription',
            'extrainfo',
            'author',
            'deadline',
            'updated',
            'created',
        ]
        """