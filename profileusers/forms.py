from django import forms
from .models import Profileuser


class ProfileuserForm(forms.ModelForm):
    class Meta:
        model = Profileuser
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone': 'Phone Number',

            'avatar': 'Profile picture',
            'image_url': 'Profile picture',
            'background': 'Profile picture',

            'firstname': 'Firstname',
            'lastname': 'Lastname',
            'title': 'Title',
            'company_name': 'Company Name picture',
            'company_number_vat': 'Company VAT no.',
            # industry = models.ForeignKey(
            #     'Industry', null=True, on_delete=models.SET_NULL, blank=True, default=None)
            'profession': 'Profession',
            'skill': 'Skills',
            'description': 'Bio',

            'email': 'Email',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
        }

        self.fields['firstname'].attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
