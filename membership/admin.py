"""
from django.contrib import admin
from .models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'membership_type',
        'price',
        'stripe_price_id',
    )

<<<<<<< HEAD
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'membership_type',
        'price',
        'stripe_price_id',
    )

=======
>>>>>>> 0ad3775 (Setup Admin membership view.)
    ordering = ('membership_type',)

class UserMembershipAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'membership',
        'stripe_customer_id',
<<<<<<< HEAD
    )

    ordering = ('user',)
    """

# admin.site.register(Membership, ProductAdmin)
# admin.site.register(UserMembership, UserMembershipAdmin)
=======
        'status',
    )
    ordering = ('user',)

admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
>>>>>>> 0ad3775 (Setup Admin membership view.)
# admin.site.register(Subscription)