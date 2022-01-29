""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class SetupViewTestCase(TestCase):
    """ Base test case to be used in all PostUpdateView view tests """
    def setUp(self):
        self.username = 'joe'
        self.password = '12345'
        user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')

class OrderView(SetupViewTestCase):
    def test_order_view_success_status_code(self):
        """ Test response on order view by url """
        url = reverse('checkout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
