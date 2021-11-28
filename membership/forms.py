from django.contrib.auth.models import User
from django import forms
from .models import Membership, UserMembership


class MembershipForm(forms.ModelForm):

    class Meta:
        model = Membership
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserMembershipForm(forms.ModelForm):

    class Meta:
        model = UserMembership
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
