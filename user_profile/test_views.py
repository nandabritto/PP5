""" System Module """
from django.urls import reverse
from order.test_views import SetupModelTestCase


class TestGetProfile(SetupModelTestCase):
    """
    Checkout test class using payload from setup model class
    """
    def test_get_profile(self):
        """
        Test if profile is created
        """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_updateprofile_if_form_is_valid(self):
        """
        Test update profile
        """
        payload = {
            'address1': 'Apartment 2356',
            'address2': 'Parnell Street 298',
            'county': 'Dublin 8',
            'country': 'IE',
            'eircode': '123457',
            'address_type': 'S',
        }
        self.client.get(reverse('update_profile'))
        response = self.client.post(reverse('update_profile'), payload)
        self.assertEqual(response.status_code, 302)

    def test_updateprofile_if_form_is_duplicated(self):
        """
        Test update profile
        """
        payload = {
            'address1': 'Apartment 2',
            'address2': 'Parnell Street 2',
            'county': 'Dublin 2',
            'country': 'IE',
            'eircode': '123456',
            'address_type': 'S',
        }
        self.client.get(reverse('update_profile'))
        response = self.client.post(reverse('update_profile'), payload)
        self.assertEqual(response.status_code, 200)

    def test_updateprofile_if_form_is_invalid(self):
        """
        Test update profile
        """
        payload = {
            'address1': 'Apartment 2356',
            'address2': 'Parnell Street 298',
            'county': 'Dublin 8',
            'country': 'Ie',
            'eircode': '123457',
            'address_type': 'S',
        }
        response = self.client.post(reverse('update_profile'), payload)
        self.assertEqual(response.status_code, 200)
