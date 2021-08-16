from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profileuser

from django.core.files.images import get_image_dimensions



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            #'firstname',
            #'lastname',
            'username',
            'email',
            'password1',
            'password2',
        ]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profileuser
        fields = [
            'picture',
            # 'image_url',
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

"""
class SigninForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            # 'firstname',
            # 'lastname',
            'username',
            # 'email',
            'password1',
        ]

"""
class ProfileuserForm(forms.ModelForm):
    class Meta:
        model = Profileuser
        fields = [
            # 'avatar',
            'picture',
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
