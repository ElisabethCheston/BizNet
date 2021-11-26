from django.contrib import admin
from .models import Membership, UserMembership


class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'membership_type',
        'price',
        'stripe_price_id',
    )

    ordering = ('membership_type',)

class UserMembershipAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'membership',
        'stripe_customer_id',
    )

    ordering = ('user',)

admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
