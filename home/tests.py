"""
System Module
"""
from django.test import TestCase


class TestUrls(TestCase):
    """
    Test if url is loading correctly
    """
    def test_home_is_resolved(self):
        """
        Test if home view load without errors
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
