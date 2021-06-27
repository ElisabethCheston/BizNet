from django.contrib import admin
from .models import Profileuser, Industry

# Register your models here.
admin.site.register(Product, Profileuser)
admin.site.register(Category, Industry)