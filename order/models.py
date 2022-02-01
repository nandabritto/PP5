""" System Module """
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from products.models import Box
from user_profile.models import UserProfile
# import uuid


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Order(models.Model):
    """
    Create order details and link it to the user
    """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
        )
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False, null=True, blank=False)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address',
        on_delete=models.SET_NULL, blank=True, null=True)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address',
        on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """
        Return a user string
        """
        return str(self.customer)

    # @property
    # def shipping(self):
    #     """
    #     Add shipping on order
    #     """
    #     shipping = True
    #     # orderbox = self.orderbox_set.all()
    #     return shipping

    @property
    def get_cart_total(self):
        """
        Get items and in the cart and sum to create cart total price
        """
        orderitems = self.orderbox_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        """
        Get items and in the cart and sum to create cart total items
        """
        orderitems = self.orderbox_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderBox(models.Model):
    """
    Create orderbox details and quantity to add to the cart
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ordered_boxes'
        )
    box = models.ForeignKey(
        Box, on_delete=models.SET_NULL, blank=True, null=True)
    order_box = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Add correct plural name on Adress
        """
        verbose_name_plural = 'Ordered boxes'

    @property
    def get_total(self):
        """
        Multiply number of item to the box price to get total
        """
        total = self.box.box_price * self.quantity
        return total

    # @property
    # def get_order_admin(self):
    #     """
    #     """
    #     from django.urls import reverse
    #     from django.utils.html import format_html
    #     order = self.order_box.id
    #     url = reverse(f'admin:order_order_change',  args=[order] )
    #     # return f'<a href="{url}">Edit </a>'
    #     return format_html("<a href='{}'>{}</a>", url, order)

# class ShippingAddress(models.Model):
#     """
#     Create shipping details and link to the user and order
#     """
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     order = models.ForeignKey(
#         Order, on_delete=models.SET_NULL, blank=True, null=True)
#     address1 = models.CharField(max_length=100, null=True)
#     addres2 = models.CharField(max_length=100, null=True)
#     county = models.CharField(max_length=20, null=True)
#     country = models.CharField(max_length=30, null=True)
#     eircode = models.CharField(max_length=7, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         """
#         Return a string to shipping address
#         """
#         return str(self.address1)


class Address(models.Model):
    """
    Create address details and link to the user and order
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    county = models.CharField(max_length=20)
    country = CountryField(multiple=False)
    eircode = models.CharField(max_length=7)
    address_type = models.CharField(
        max_length=1,
        choices=ADDRESS_CHOICES,
        default='S')
    default = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     previous_address = self.objects.filter(
    #         customer=self.customer,
    #         address1 = self.address1,
    #         address2 = self.address2,
    #         county = self.county,
    #         country = self.country,
    #         eircode = self.eircode,
    #         address_type = self.address_type
    #         )
    #     if previous_address.exists():
    #         previous_address = self.default
    #         super(Address, previous_address).update(*args, **kwargs)
    #     else:
    #         super(Address, self).save(*args, **kwargs)

    def __str__(self):
        """
        Return a string to billing address
        """
        return str(self.customer)

    class Meta:
        """
        Add correct plural name on Adress
        """
        verbose_name_plural = 'adresses'


class Payment(models.Model):
    """
    Create stripe payment
    """
    stripe_charge_id = models.CharField(max_length=50)
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string to payment
        """
        return self.customer.username
