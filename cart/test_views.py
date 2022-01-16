""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth
import logging


class SetupViewTestCase(TestCase):
    """
    Test cart views
    """
    def setup(self):
        self.username = 'joe'
        self.password = '12345'
        user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')
        logging.debug(self.username)
    


class TestCart(SetupViewTestCase):
    def test_if_user_is_autheticated(self):
        user = auth.get_user(self.client)
        self.assertIn('joe', self.client.session)
        
