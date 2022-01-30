""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Order, OrderBox, Address, Payment
from products.models import Box
from .forms import CheckoutForm


class SetupModelTestCase(TestCase):
    """ Base test case to be used in all models tests """

    def setUp(self):
        """ Setup for testing models """
        self.username = 'joe'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')
        self.billing_address1=Address.objects.create(
            customer = self.user,
            address1 = 'Apartment 1',
            address2 = 'Parnell Street',
            county = 'Dublin',
            country = 'Ie',
            eircode = '12345',
            address_type = 'B',
            default = 'True'
        )
        self.shipping_address1=Address.objects.create(
            customer = self.user,
            address1 = 'Apartment 2',
            address2 = 'Parnell Street 2',
            county = 'Dublin 2',
            country = 'Ie',
            eircode = '123456',
            address_type = 'S',
            default = 'True'
        )
        self.payment1= Payment.objects.create(
            stripe_charge_id= '123456789',
            customer = self.user,
            amount='900',
            timestamp= '1643316725'
        )
        self.order1 = Order.objects.create(
            customer=self.user,
            date_ordered='Oct. 24, 2021, 8:52 p.m.',
            billing_address = self.billing_address1,
            shipping_address = self.shipping_address1
            )
        self.shipping = True
        """
        Box creation
        """
        self.box1 = Box.objects.create(box_name='testBox1', box_price=float('49.99'),  category='Countries', box_description='test Box 1')
        # self.order1 = Order.objects.create(customer,date_ordered,billing_address,shipping_address,payment)
        self.orderbox1 = OrderBox.objects.create(box=self.box1,order_box=self.order1,quantity=int('2'))

        self.checkout = {
                    'shipping_address1': self.shipping_address1.address1,
                    'shipping_address2': self.shipping_address1.address2,
                    'shipping_county': self.shipping_address1.county,
                    'shipping_country': self.shipping_address1.country,
                    'shipping_eircode': self.shipping_address1.eircode,
                    'billing_address1': self.billing_address1.address1,
                    'billing_address2':self.billing_address1.address2,
                    'billing_county': self.billing_address1.county,
                    'billing_country': self.billing_address1.country,
                    'billing_eircode': self.billing_address1.eircode,
                    # 'same_billing_address': False,
                    # 'set_default_shipping': False,
                    # 'use_default_shipping': False,
                    # 'set_default_billing': False,
                    # 'use_default_billing': False
                    }

class TestCheckoutView(SetupModelTestCase):
    def setUp(self):
        """ Setup user and review from SetupViewTestCase """
        super().setUp()
    
    
    def test_post_if_form_is_valid(self):
        """
        Check if checkout data is correct and
        save checkout info
        """
        payload = self.checkout

        response = self.client.post(reverse('checkout'), payload)
        self.assertEqual(response.status_code, 302)
        
    def test_post_if_form_is_valid_default_shipping(self):
        """
        Check if checkout data is correct and
        use default shiping address
        """
        self.checkout['use_default_shipping'] = True
        payload = self.checkout

        response = self.client.post(reverse('checkout'), payload)
        self.assertEqual(response.status_code, 302)
        
    def test_post_if_form_is_valid_set_default_shipping(self):
        """
        Check if checkout data is correct and
        use default shiping address
        """
        self.checkout['set_default_shipping'] = True
        payload = self.checkout

        response = self.client.post(reverse('checkout'), payload)
        self.assertEqual(response.status_code, 302)

    def test_post_if_form_is_not_valid_set_default_shipping(self):
        """
        Check if checkout data is correct and
        there is no default shiping address
        """
        
        print(self.shipping_address1.default)
        self.shipping_address1.default = False
        self.shipping_address1.save()
        print(self.shipping_address1.default)
        self.checkout['use_default_shipping'] = True

        payload = {'use_default_shipping': True, 'use_default_billing':True}

        response = self.client.post(reverse('checkout'), payload)
        self.assertEqual(response.status_code, 302)