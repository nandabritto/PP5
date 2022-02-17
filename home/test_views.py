""" System Module """
from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
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
