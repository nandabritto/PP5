from django.test import TestCase
from django.urls import reverse
from .models import Box
from .views import product_detail

class TestViews(TestCase):

    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        Box.objects.create(box_name='BoxTest')
                
        
    def test_boxes_view(self):
        """ Test redirect if user is invalid is correct """
        boxes = Box.objects.all()
        response = self.client.get(reverse('boxes'))
        self.assertEqual(response.status_code, 200)


    def test_product_detail_view(self):
        # response = self.client.get(reverse('product_detail', kwargs={
        #     'pk': 1}))
        # self.assertEqual(response.status_code, 200)