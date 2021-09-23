from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profileuser, Industry, Profession, Employment, Status, Skills, Business
from gigs.models import Gig

from django.core.files.images import get_image_dimensions
from django.http import JsonResponse
import json
import urllib.parse



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
        ]
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    industry = forms.ModelChoiceField(queryset=Industry.objects.all(), empty_label='Industry:')
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label='Profession:')
    description = forms.CharField(label='description',widget=forms.TextInput(attrs={'placeholder':'Description: Who are of You'}))
    employment = forms.ModelChoiceField(queryset=Employment.objects.all(), empty_label='Employment Status:')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='Purpose:')
    business = forms.ModelChoiceField(queryset=Business.objects.all(), empty_label='Business:')
    # skills = forms.ModelChoiceField(queryset=Skills.objects.all(), empty_label='Skills:')
    # countries = forms.ModelChoiceField(queryset=Countries.objects.all(), empty_label='Countries:')
    # locations = forms.ModelChoiceField(queryset=Locations.objects.all(), empty_label='Locations:')

    class Meta:
        model = Profileuser
        fields = [
            'avatar',
            'picture',
            #'first_name',
            #'last_name',
            'title',
            'company_name',
            #'company_number_vat',
            'industry',
            'profession',
            # 'skill',
            'description',
            # 'phone',
            #'email',
            'country',
            'city',
            'locations',
            # 'skills',
            'employment',
            'business',
            'status',
        ]
"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
 
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('city')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk and self.instance.country:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
"""

class ProfileForm1(forms.ModelForm):

    # country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Country:')
    # city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label='City:')

    class Meta:
        model = Profileuser
        fields = [
            'avatar',
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
    # skills = forms.ModelChoiceField(queryset=Skills.objects.all(), empty_label='Skills:')
    # countries = forms.ModelChoiceField(queryset=Countries.objects.all(), empty_label='Countries:')
    # youremployment = forms.ModelChoiceField(queryset=yourEmployment.objects.all(), empty_label='Employment')
    # yourstatus = forms.ModelChoiceField(queryset=yourStatus.objects.all(), empty_label='Am looking for..')
    # locations = forms.ModelChoiceField(queryset=Locations.objects.all(), empty_label='Locations:')

    class Meta:
        model = Profileuser
        fields = [
            'business',
            # 'skills',
            'locations',
            # 'youremployment',
            # 'yourstatus',
        ]


"""
class GigForm(model.Model):
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

