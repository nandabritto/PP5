from django.contrib import admin
from .models import Order, OrderBox, Address, Payment


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'address1',
        'address2',
        'county',
        'country',
        'eircode',
        'address_type',
        'default'
    ]

    list_filter = [ 'country', 'default', 'address_type']
    search_fields = [ 'customer', 'address1', 'eircode']



admin.site.register(Order)
admin.site.register(OrderBox)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)