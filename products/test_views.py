from django.test import TestCase
from django.urls import reverse
from .models import Box
from .views import product_detail

class TestViews(TestCase):

    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.boxtest = Box.objects.create(box_name='BoxTest', category='test', box_price='49.99', box_description='Test' , box_image='noimage.jpg')
                
        
    def test_boxes_view(self):
        """ Test redirect if user is invalid is correct """
        response = self.client.get(reverse('boxes'))
        self.assertEqual(response.status_code, 200)


    def test_product_detail_view(self):
        url = reverse('product_details', kwargs={
            'pk': self.boxtest.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)