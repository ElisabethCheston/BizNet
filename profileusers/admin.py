from django.contrib import admin
from .models import Profileuser, Industry, Profession, Skills, Business


# Register your models here.
admin.site.register(Profileuser)
admin.site.register(Industry)
admin.site.register(Profession)
admin.site.register(Skills)
admin.site.register(Business)
