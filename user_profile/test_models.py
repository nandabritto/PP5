""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Box
from .models import UserProfile, Address


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
            country='Ie',
            eircode='123456',
            address_type='S'
        )

class UserProfileTestCase(SetupModelTestCase):
    """
    Test UserProfile model function
    """
    def test__str__(self):
        """
        Test if UserProfile is returning correct string
        """
        profile = UserProfile.objects.get(
            customer=self.user
        )
        self.assertEqual(str(profile), 'joe')