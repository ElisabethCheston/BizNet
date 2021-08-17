from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Profileuser

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

class EditForm(UserChangeForm):
    class Meta:
        model = Profileuser
        fields = [
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
