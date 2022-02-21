""" System Module """
from django.test import TestCase
from decimal import Decimal
from django.contrib.auth.models import User
from products.models import Box
from .models import Order, OrderBox, Address, Payment


class SetupModelTestCase(TestCase):
    """
    Base test case to be used in all models tests
    """
    def setUp(self):
        """ Setup for testing models """
        self.username = 'joe'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')
        self.billing_address1 = Address.objects.create(
            customer=self.user,
            address1='Apartment 1',
            address2='Parnell Street',
            county='Dublin',
            country='Ie',
            eircode='12345',
            address_type='B',
            default='True'
        )
        self.shipping_address1 = Address.objects.create(
            customer=self.user,
            address1='Apartment 2',
            address2='Parnell Street 2',
            county='Dublin 2',
            country='IE',
            eircode='123456',
            address_type='S'
        )
        self.shipping_address2 = Address.objects.create(
            customer=self.user,
            address1='Apartment 21',
            address2='Street 2',
            county='Rio de Janeiro',
            country='BR',
            eircode='654321',
            address_type='S'
        )
        self.payment1 = Payment.objects.create(
            stripe_charge_id='123456789',
            customer=self.user,
            amount='900',
            timestamp='1643316725'
        )
        self.order1 = Order.objects.create(
            customer=self.user,
            date_ordered='Oct. 24, 2021, 8:52 p.m.',
            billing_address=self.billing_address1,
            shipping_address=self.shipping_address1
            )
        self.shipping = True
        # Box creation
        self.box1 = Box.objects.create(
            box_name='testBox1',
            box_price=float('49.99'),
            category='Countries',
            box_description='test Box 1')
        self.orderbox1 = OrderBox.objects.create(
            box=self.box1,
            order_box=self.order1,
            quantity=int('2')
            )


class OrderTestCase(SetupModelTestCase):
    """
    Test Order model function
    """
    def test__str__(self):
        """
        Test if order is returning correct string
        """
        self.assertEqual(str(self.order1), 'joe')


class AddressTestCase(SetupModelTestCase):
    """
    Test Address model function
    """
    def test__str__(self):
        """
        Test if address is returning correct string
        """
        self.assertEqual(str(self.shipping_address1), 'joe')


class PaymentTestCase(SetupModelTestCase):
    """
    Test Order model function
    """
    def test__str__(self):
        """
        Test if order is returning correct string
        """
        self.assertEqual(str(self.payment1), 'joe')


class OrderBoxGetTotalTestCase(SetupModelTestCase):
    """
    Test get ordered box total
    """
    def test_get_total(self):
        """
        Test get total property
        """
        self.assertEqual(self.orderbox1.get_total, float('99.98'))


class OrderBoxGetShipping(SetupModelTestCase):
    """
    Test get shipping
    """
    def test_get_shipping(self):
        """
        Test get shipping property
        """
        self.order1.shipping_address = self.shipping_address2
        self.assertEqual(self.order1.get_cart_total, Decimal('114.98'))

    def test_get_shipping_none(self):
        """
        Test get shipping property when its none
        """
        self.order1.shipping_address = None
        self.assertEqual(self.order1.get_cart_total, Decimal('99.98'))
