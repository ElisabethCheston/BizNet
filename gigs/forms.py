# from django.contrib.auth.models import User
from django import forms
from .models import Gig
from profileusers.models import Profileuser, Industry, Profession


class GigForm(forms.ModelForm):
    # industry = forms.ModelChoiceField(queryset=Industry.objects.all(), empty_label='Industry:')
    # profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label='Profession:')

    class Meta:
        model = Gig
        fields = [
            'title',
            'industry',
            'profession',
            'city',
            'country',
            'gigdescription',
            'extrainfo',
            'author',
            'deadline',
            # 'updated',
            # 'created',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-control'}),

            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

            'gigdescription': forms.Textarea(attrs={'class': 'form-control'}),
            'extrainfo': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(
                format=('%Y-%m-%d'), attrs={
                    'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
        }


"""
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