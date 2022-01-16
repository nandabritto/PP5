""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User


class CartTestCase(TestCase):
    """
    Test cart views
    """
    def test_cart_view(self):
        self.username = 'joe'
        self.password = '12345'
        user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')
        
    
        