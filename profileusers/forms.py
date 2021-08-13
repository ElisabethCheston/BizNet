from django.contrib.auth.models import User
from django import forms
from .models import Profileuser

from django.core.files.images import get_image_dimensions


class ProfileuserForm(forms.ModelForm):
    class Meta:
        model = Profileuser
        fields = [
            'avatar',
            'picture',
            'background',
            'firstname',
            'lastname',
            'title',
            'company_name',
            'company_number_vat',
            'industry',
            'profession',
            'skill',
            'description',
            'phone',
            'email',
            'city',
            'country',
        ]
        

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profileuser
        fields = [
            'avatar',
            # 'image_url',
            'background',
            'firstname',
            'lastname',
            'title',
            'company_name',
            'company_number_vat',
            'industry',
            'profession',
            'skill',
            'description',
            'phone',
            'email',
            'city',
            'country',
        ]