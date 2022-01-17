""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from products.models import Box


class SetupViewTestCase(TestCase):
    """
    Test cart views
    """
    def setUp(self):
        self.username = 'joe'
        self.password = '12345'
        user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')
        self.box = Box.objects.create(
            box_name='Test Box',
            box_price='10.99',
            category='Test Category',
            box_description='test Description',
            box_image='testimage.jpg')


class TestCart(SetupViewTestCase):
    """
    Test cart function
    """
    def test_if_user_is_autheticated(self):
        """
        Check if user can authenticate
        """
        self.client.login(username='joe', password='12345')
        user = auth.get_user(self.client)

    def test_cart_view_url_if_authenticated(self):
        """
        Test response on cart view if user is authenticated
        """
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

    def test_cart_view_url_if_not_authenticated(self):
        """
        Test response on cart view if user is not authenticated
        """
        self.client.logout()
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)


class TestUpdateCart(SetupViewTestCase):
    """
    Test updatecart function
    """
    def test_update_cart_add(self):
        """
        Test if products are loadng in shopping cart
        """
        payload = {'boxId': self.box.id, 'action': 'add'}
        response = self.client.post(
            reverse('update_cart'),
            data=payload,
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_add_or_remove_item_to_cart(self):
        """
        Test if user can add or remove items to the shopping cart
        """
        payload = {'boxId': self.box.id, 'action': 'add'}
        response = self.client.post(reverse(
            'update_cart'),
            data=payload,
            content_type='application/json')
        payload = {'boxId': self.box.id, 'action': 'remove'}
        response = self.client.post(reverse(
            'update_cart'),
            data=payload,
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
