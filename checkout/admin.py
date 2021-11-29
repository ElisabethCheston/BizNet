from django.contrib import admin
from .models import Subscription, SubscriptionLineItem


class SubscriptionLineItemAdminInline(admin.TabularInline):
    model = SubscriptionLineItem
    readonly_fields = ('lineitem_total',)


class SubscriptionAdmin(admin.ModelAdmin):
    inlines = (SubscriptionLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'order_total',
        'grand_total',
        'stripe_pid'
        )

    fields = (
        'order_number',
        'user_profile',
        'date',
        'full_name',
        'email',
        'order_total',
        'grand_total',
        'stripe_pid'
        )

    list_display = (
        'user_profile', 
        'order_number', 
        'full_name',
        'order_total', 
        'grand_total', 
        'stripe_pid',
    )

    ordering = ('-date',)

admin.site.register(Subscription, SubscriptionAdmin)
