from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profileuser, Countries, Cities, Industry, Profession, Skills, Business

from django.core.files.images import get_image_dimensions



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
            'skill',
            'description',
            'phone',
            #'email',
            'city',
            'country',
            'countries',
            'cities',
            'skills',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cities'].queryset = Cities.objects.none()

        if 'countries' in self.data:
            try:
                countries_id = int(self.data.get('countries'))
                self.fields['cities'].queryset = Cities.objects.filter(countries_id=countries_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Cities queryset
        elif self.instance.pk:
            self.fields['cities'].queryset = self.instance.countries.cities_set.order_by('name')


class ProfileForm1(forms.ModelForm):
    class Meta:
        model = Profileuser
        fields = [
            # 'avatar',
            'picture',
            # 'firstname',
            # 'lastname',
            'title',
            'company_name',
            'company_number_vat',
            'phone',
            # 'email',
            'city',
            'country',
        ]


class ProfileForm2(forms.ModelForm):
    industry = forms.ModelChoiceField(queryset=Industry.objects.all(), empty_label='Industry')
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label='Profession')
    description = forms.CharField(label='description',widget=forms.TextInput(attrs={'placeholder':'Description: Who are of You'}))
    
    class Meta:
        model = Profileuser
        fields = ['industry', 'profession', 'description']



class ProfileForm3(forms.ModelForm):
    business = forms.ModelChoiceField(queryset=Business.objects.all(), empty_label='Industry:')
    skills = forms.ModelChoiceField(queryset=Skills.objects.all(), empty_label='Skills:')
    countries = forms.ModelChoiceField(queryset=Countries.objects.all(), empty_label='Countries:')
    cities = forms.ModelChoiceField(queryset=Cities.objects.all(), empty_label='Cities:')
   # locations = forms.ModelChoiceField(queryset=Locations.objects.all(), empty_label='Skills')
    
    class Meta:
        model = Profileuser
        fields = [
            'business',
            'skills',
            'countries',
            'cities',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cities'].queryset = Cities.objects.all()

        if 'countries' in self.data:
            try:
                countries_id = int(self.data.get('countries'))
                self.fields['cities'].queryset = Cities.objects.filter(countries_id=countries_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Cities queryset
        elif self.instance.pk:
            self.fields['cities'].queryset = self.instance.countries.cities_set.order_by('name')


"""
class ProfileForm3(forms.ModelForm):
    class Meta:
        model = Profileuser
        fields = [
            'business',
            'skills',
            #'city',
            'locations',
        ]
"""