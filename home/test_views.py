""" System Module """
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User



class TestViews(TestCase):
    """
    Test if url is loading correctly
    """
    def test_home_is_resolved(self):
        """
        Test if home view load without errors
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class TestStaffUser(TestCase):
    """
    Test if user is staff
    """
    def test_staff_user(self):
        """
        Test if logged user is staff
        """
        user = User.objects.create_user('joe', 'joe@example.com', '12345')  
        user.is_staff = True 
        user.save()
        self.client.login(username='joe', password='12345')
        response = self.client.get(reverse('management'))
        self.assertEqual(response.status_code, 200)

    def test_customer_user_access_page(self):
        """
        Test if logged user is staff
        """
        user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('management'))
        self.assertEqual(response.status_code, 403)
