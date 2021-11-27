from django.contrib import admin
from .models import Subscription, SubscriptionLineItem


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile', 
        'order_number', 
        'full_name', 
        'membership', 
        'stripe_customer_id', 
        'email', 
        'date',
        'order_total', 
        'grand_total', 
        'original_bag',
        'stripe_pid',
    )

    ordering = ('membership',)

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(SubscriptionLineItem)
