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
            'position',
            'overview',
            'requirements',
            'contact',
            # 'author',
            'deadline',
            # 'updated',
            # 'created',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'industry': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            'profession': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Profession'}),

            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'country': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'position': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Position (250 characters)'}),
            'overview': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Company Overview (250 characters)'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Requirements (250 characters)'}),
            'contact': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Send you CV and cover letter to..'}),
            'deadline': forms.DateInput(
                format=('%Y-%m-%d'), attrs={
                    'class': 'form-control', 
                    'placeholder': 'Deadline Date',
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