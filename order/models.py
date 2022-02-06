""" System Module """
from django.db import models
from django.contrib.auth.models import User
# from django_countries.fields import CountryField
from products.models import Box
from user_profile.models import UserProfile, Address


class Order(models.Model):
    """
    Create order details and link it to the user
    """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    # user_profile = models.ForeignKey(
    #     UserProfile,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='orders'
    #     )
  
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False, null=True, blank=False)
    billing_address = models.ForeignKey(
        'user_profile.Address', related_name='billing_address',
        on_delete=models.SET_NULL, blank=True, null=True)
    shipping_address = models.ForeignKey(
        'user_profile.Address', related_name='shipping_address',
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
    # user_profile = models.ForeignKey(
    #     UserProfile,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='ordered_boxes'
    #     )
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
