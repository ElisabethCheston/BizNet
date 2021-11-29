from profileusers.models import Profileuser, Industry, Profession, Employment, Status, Skills, Business, TermUser
from gigs.models import Gig
import json
import urllib.parse

from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.forms.widgets import CheckboxInput



# -- REGISTRATION USER FORM -- #

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            # 'agree',
        ]

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class TermsForm(forms.ModelForm):
    class Meta:
        model = TermUser
        fields = [
            'agree',
        ]

        widgets = {
            'agree': CheckboxInput(attrs={'class': 'agree'}),
        }


# -- EDIT FORM IN PROFILE -- #

class ProfileForm(forms.ModelForm):
    industry = forms.ModelChoiceField(queryset=Industry.objects.all(), empty_label='Industry:')
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label='Profession:')
    description = forms.CharField(label='description',widget=forms.TextInput(attrs={'placeholder':'Description: Who are of You'}))
    employment = forms.ModelChoiceField(queryset=Employment.objects.all(), empty_label='Employment Status:')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='Purpose:')
    business = forms.ModelChoiceField(queryset=Business.objects.all(), empty_label='Business:')

    class Meta:
        model = Profileuser
        fields = [
            'avatar',
            'picture',
            'title',
            'company_name',
            'industry',
            'profession',
            'description',
            'country',
            'city',
            'locations',
            'employment',
            'business',
            'status',
        ]


# -- REGISTRATION FORM FOR PROFILE -- #

class ProfileForm1(forms.ModelForm):

    class Meta:
        model = Profileuser
        fields = [
            'picture',
            'title',
            'company_name',
            'country',
            'city',
        ]


class ProfileForm2(forms.ModelForm):
    industry = forms.ModelChoiceField(queryset=Industry.objects.all(), empty_label='Industry:')
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label='Profession:')
    description = forms.CharField(label='description',widget=forms.TextInput(attrs={'placeholder':'Description: Who are of You'}))
    employment = forms.ModelChoiceField(queryset=Employment.objects.all(), empty_label='Employment Status:')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='Purpose:')
    
    class Meta:
        model = Profileuser
        fields = [
            'industry',
            'profession',
            'description',
            'employment',
            'status',
            ]


class ProfileForm3(forms.ModelForm):
    business = forms.ModelChoiceField(queryset=Business.objects.all(), empty_label='Business:')

    class Meta:
        model = Profileuser
        fields = [
            'business',
            'locations',
        ]
