""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Order, OrderBox, Address, Payment

class SetupModelTestCase(TestCase):
    """ Base test case to be used in all models tests """

    def setUp(self):
        """ Setup for testing models """
        self.username = 'joe'
        self.password = '12345'
        user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')
        # self.billing_address=Address.objects.create(
        #     customer = user,
        #     address1 = 'Apartment 1',
        #     address2 = 'Parnell Street',
        #     county = 'Dublin',
        #     country = 'Ireland',
        #     eircode = '123456',
        #     address_type = 'B'
        # )
        # self.shipping_address=Address.objects.create(
        #     customer = user,
        #     address1 = 'Apartment 2',
        #     address2 = 'Parnell Street 2',
        #     county = 'Dublin 2',
        #     country = 'Ireland',
        #     eircode = '123456',
        #     address_type = 'S'
        # )
        self.payment= Payment.objects.create(
            stripe_charge_id= '123456789',
            customer = user,
            amount='900',
            timestamp= '1643316725'
        )
        self.order = Order.objects.create(
            customer=user,
            date_ordered='Oct. 24, 2021, 8:52 p.m.',
            # billing_address = self.billing_address,
            # shipping_address = self.shipping_address,
            payment=self.payment
        )
    
class OrderTestCase(SetupModelTestCase):
    """ Test BeerReview model functions """
    def test__str__(self):
        """ Test if review is returning all model objetcs and pk """
        self.assertEqual(str(self.user))
