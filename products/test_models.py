from django.test import TestCase
from .models import Product, Box, Product_On_Box
import logging

class TestProduct(TestCase):
    """
    Test Product model function
    """
    def test_create_products(self):
        """
        Test product creation
        """
        self.product_name = Product.objects.create(product_name='ProductTest')
        self.product_price = Product.objects.create(product_price='2.99')
        self.product_description = Product.objects.create(product_description='This is a test description')
        self.product_image = Product.objects.create(product_image='noimage.jpg')

    def test__str__(self):
        """
        Test if Product is returning lower string
        """
        self.product_name = Product.objects.create(product_name='ProductTest')
        self.assertEqual(str(self.product_name), self.product_name.product_name.lower())


class TestBox(TestCase):
    """
    Test Box model function
    """
    def test_create_box(self):
        """
        Test box creation
        """
        self.box_name = Box.objects.create(box_name='BoxName')
        
    def test__str__(self):
        """
        Test if Box is returning lower string
        """
        self.box_name = Box.objects.create(box_name='BoxName')
        self.assertEqual(str(self.box_name), self.box_name.box_name.lower())

class TestProductOnBox(TestCase):
    """
    Test Product_On_Box model function
    """
    def test_product_on_box(self):
        """
        Test product on box creation
        """
        self.product_name = Product.objects.create(product_name='ProductTest')
        self.box_name = Box.objects.create(box_name='BoxName')
        self.product = self.product_name
        self.box = self.box_name

    def test__str__(self):
        """
        Test if Box is returning lower string
        """
        self.box = Box.objects.create(box_name='BoxName')
        self.product = Product.objects.create(product_name='ProductTest')
        self.product_on_box = Product_On_Box.objects.create(
            product=self.product, box=self.box, product_selectable=True)
        self.assertEqual(str(str(self.product_on_box)), f"{self.box.box_name} | {self.product.product_name}")
        # self.assertEqual(str(self.box,self.box_name.box_name.lower())
        # self.assertEqual(str(self.box_name), self.box_name.box_name.lower())
    