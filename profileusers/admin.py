from django.contrib import admin
from .models import Profileuser, Industry


class ProfilesAdmin(admin.ModelAdmin):

    fields = (
        'username',
        'password',
        'firstname',
        'lastname',
        'title',
        'company_name',
        'company_number_vat',
        # 'industry',
        'profession',
        'skill',     
        'description',
        'image_url',
        'image',
        'email',
        'phone',
        'city',
        'country',
    )

    list_display = (
        'user_id',
        'username',
        'password',
        'firstname',
        'lastname',
        'title',
        'company_name',
        'company_number_vat',
        # 'industry',
        'profession',
        'skill',     
        'description',
        'image_url',
        'image',
        'email',
        'phone',
        'city',
        'country',
    )


class IndustryAdmin(admin.ModelAdmin):
    list_display = (
        'prof_name',
    )


# Register your models here.
admin.site.register(Profileuser, ProfilesAdmin)
admin.site.register(Industry, IndustryAdmin)