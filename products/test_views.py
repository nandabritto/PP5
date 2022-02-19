""" System Module """
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Box, Product, Product_On_Box
from product_review.models import BoxReview


class SetupModelTestCase(TestCase):
    """
    A class to test all views
    """
    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.username = 'joe'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.user.is_staff = True 
        self.user.save()
        self.client.login(username='joe', password='12345')
        self.boxtest = Box.objects.create(
            box_name='BoxTest',
            category='test',
            box_price='49.99',
            box_description='Test',
            box_image='acafran.jpg')
        self.producttest = Product.objects.create(
            product_name='ProductTest',
            product_description='test',
            product_price='49.99',
            product_image='acafran.jpg')
        self.productonboxtest = Product_On_Box.objects.create(
            product=self.producttest,
            box=self.boxtest,
            product_selectable=True,
            )
        self.boxreview = BoxReview.objects.create(
            customer=self.user,
           box=self.boxtest,
           review_text='Review Text Sample',
           review_rating='5',
        )

class TestViews(SetupModelTestCase):
    """
    Test views in products app
    """
    def test_boxes_view(self):
        """
        Test if render boxes template and objects is correct
        """
        response = self.client.get(reverse('boxes'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """
        Test if render correctly product details view with correct
        box and product pk
        """
        url = reverse('box_details', kwargs={
            'pk': self.boxtest.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class BoxDetailTestCase(SetupModelTestCase):
    """
    Test post review in box_detail page
    """
    def test_box_detail_post_review(self):
        """
        Test if user is authenticated and add review
        """
        payload = {
           'customer':self.user,
           'box': self.boxtest,
           'review_text':'Review Text',
           'review_rating':'5',
        }
        response = self.client.post(reverse('box_details', kwargs={
            'pk': self.boxtest.id}), payload)
        self.assertEqual(response.status_code, 302)


class ProductDetailTestCase(SetupModelTestCase):
    """
    Test product detail page
    """
    def test_product_detail_correct_view(self):
        """
        Test if product detail uses correct view
        """
        response = self.client.get(reverse('product_details', kwargs={
            'pk': self.producttest.id}))
        self.assertEqual(response.status_code, 200)


class AddBoxTestCase(SetupModelTestCase):
    """
    Test Add box page
    """
    def test_post_if_form_is_valid(self):
        """
        Test add box post if form is valid
        """
        payload = {
           'box_name':self.boxtest.box_name,
           'box_price':self.boxtest.box_price,
           'category':self.boxtest.category,
           'box_description': self.boxtest.box_description,
           'box_image':self.boxtest.box_image
        }
        response = self.client.post(reverse('add_box'), payload)
        self.assertEqual(response.status_code, 302)

    def test_post_if_form_is_invalid(self):
        """
        Test add box post if form is invalid
        """
        payload = {
           'box_name':self.boxtest.box_name,
           'box_price':self.boxtest.box_price,
           'category':'',
           'box_description': self.boxtest.box_description,
           'box_image':''
        }
        response = self.client.post(reverse('add_box'), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_addbox_form(self):
        """
        Test add box get right form
        """
        response = self.client.get(reverse('add_box'))
        self.assertEqual(response.status_code, 200)

    def test_get_addboxform_customer_user(self):
        """
        Test add box form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('add_box'))
        self.assertEqual(response.status_code, 200)


class AddProductTestCase(SetupModelTestCase):
    """
    Test Add produc page
    """
    def test_post_if_form_is_valid(self):
        """
        Test add product post if form is valid
        """
        payload = {
           'product_name':self.producttest.product_name,
           'product_price':self.producttest.product_price,
           'product_description': self.producttest.product_description,
           'product_image':self.producttest.product_image
        }
        response = self.client.post(reverse('add_product'), payload)
        self.assertEqual(response.status_code, 302)

    def test_post_if_form_is_invalid(self):
        """
        Test add box post if form is invalid
        """
        payload = {
           'product_name':'',
           'product_price':self.producttest.product_price,
           'product_description': self.producttest.product_description,
           'product_image':''
        }
        response = self.client.post(reverse('add_product'), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_addproduct_form(self):
        """
        Test add produtc get right form
        """
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)

    def test_get_addproductform_customer_user(self):
        """
        Test add product form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)



class AddProductOnBoxTestCase(SetupModelTestCase):
    """
    Test Add product on box page
    """
    def test_post_if_form_is_valid(self):
        """
        Test add product on box post if form is valid
        """
        payload = {
           'product':self.producttest.id,
           'box':self.boxtest.id,
           'product_selectable':'on'
        }
        response = self.client.post(reverse('add_product_box'), payload)
        self.assertEqual(response.status_code, 200)

    def test_post_if_form_is_invalid(self):
        """
        Test add box post if form is invalid
        """
        payload = {
           'product_name':'',
           'product_price':self.producttest.product_price,
           'product_description': self.producttest.product_description,
           'product_image':''
        }
        response = self.client.post(reverse('add_product_box'), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_addproductonbox_form(self):
        """
        Test add product on box get right form
        """
        response = self.client.get(reverse('add_product_box'))
        self.assertEqual(response.status_code, 200)

    def test_get_addproductonboxform_customer_user(self):
        """
        Test add product form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('add_product_box'))
        self.assertEqual(response.status_code, 200)


class EditProductOnBoxTestCase(SetupModelTestCase):
    """
    Test Edit product on box page
    """
    def test_edit_on_box_post_if_form_is_valid(self):
        """
        Test edit product on box post if form is valid
        """
        payload = {
           'product':'1',
           'box':'1',
           'product_selectable':self.productonboxtest.product_selectable
        }

        response = self.client.post(reverse('editproductonbox', kwargs={
            'pk': self.productonboxtest.id}), payload)
        self.assertEqual(response.status_code, 200)

    def test_product_on_box_post_if_form_is_invalid(self):
        """
        Test edit box post if form is invalid
        """
        payload = {
           'product':self.productonboxtest.id,
           'box':'',
           'product_selectable':self.productonboxtest.product_selectable
        }
       
        response = self.client.post(reverse('editproductonbox', kwargs={
            'pk': self.productonboxtest.id}), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_edit_product_on_box_form(self):
        """
        Test edit product on box get right form
        """
        response = self.client.get(reverse('editproductonbox', kwargs={
            'pk': self.productonboxtest.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_edit_product_on_box_form_customer_user(self):
        """
        Test edit product form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('editproductonbox', kwargs={
            'pk': self.productonboxtest.id}))
        self.assertEqual(response.status_code, 200)

class EditBoxTestCase(SetupModelTestCase):
    """
    Test Edit Box page
    """
    def test_edit_box_post_if_form_is_valid(self):
        """
        Test edit box post if form is valid
        """
        payload = {
           'box_name':'Name',
           'box_price':self.boxtest.box_price,
           'category':self.boxtest.category,
           'box_description': self.boxtest.box_description,
           'box_image':self.boxtest.box_image
        }
        response = self.client.post(reverse('edit_box', kwargs={
            'pk': self.boxtest.id}), payload)
        self.assertEqual(response.status_code, 200)


    def test_edit_box_post_if_form_is_invalid(self):
        """
        Test edit box post if form is invalid
        """
        payload = {
           'box_name':'',
           'box_price':self.boxtest.box_price,
           'category':self.boxtest.category,
           'box_description': self.boxtest.box_description,
           'box_image':self.boxtest.box_image
        }
        response = self.client.post(reverse('edit_box', kwargs={
            'pk': self.boxtest.id}), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_edit_box_form(self):
        """
        Test add edit box get right form
        """
        response = self.client.get(reverse('edit_box', kwargs={
            'pk': self.boxtest.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_edit_box_form_customer_user(self):
        """
        Test edit box form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('edit_box', kwargs={
            'pk': self.boxtest.id}))
        self.assertEqual(response.status_code, 200)


class EditProductTestCase(SetupModelTestCase):
    """
    Test Edit product page
    """
    def test_edit_product_post_if_form_is_valid(self):
        """
        Test edit product post if form is valid
        """
        payload = {
           'product_name':'Name',
           'product_price':self.producttest.product_price,
           'product_description': self.producttest.product_description,
           'product_image':''
        }
        response = self.client.post(reverse('edit_product', kwargs={
            'pk': self.producttest.id}), payload)
        self.assertEqual(response.status_code, 200)


    def test_edit_box_post_if_form_is_invalid(self):
        """
        Test edit box post if form is invalid
        """
        payload = {
           'product_name':'',
           'product_price':self.producttest.product_price,
           'product_description': self.producttest.product_description,
           'product_image':''
        }
        response = self.client.post(reverse('edit_product', kwargs={
            'pk': self.producttest.id}), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_edit_product_form(self):
        """
        Test add edit product get right form
        """
        response = self.client.get(reverse('edit_product', kwargs={
            'pk': self.producttest.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_edit_product_form_customer_user(self):
        """
        Test edit product form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('edit_product', kwargs={
            'pk': self.producttest.id}))
        self.assertEqual(response.status_code, 200)


class EditReviewTestCase(SetupModelTestCase):
    """
    Test edit review page
    """
    def test_edit_review_post_form_valid(self):
        """
        Test if user is authenticated and edit review with valid form
        """
        self.client.login(username='joe', password='12345')
        payload = {
           'review_text':'Review Text 3',
           'review_rating':'5',
        }
        response = self.client.post(reverse('edit_review', kwargs={
            'pk': self.boxreview.id}), payload)
        self.assertEqual(response.status_code, 302)

    def test_edit_review_post_form_invalid(self):
        """
        Test if user is authenticated and edit review form invalid
        """
        self.client.login(username='joe', password='12345')
        payload = {
           'review_text':'',
           'review_rating':'5',
        }
        response = self.client.post(reverse('edit_review', kwargs={
            'pk': self.boxreview.id}), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_edit_review_form(self):
        """
        Test add edit review get right form
        """
        response = self.client.get(reverse('edit_review', kwargs={
            'pk': self.boxreview.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_edit_review_form__wrong_customer(self):
        """
        Test edit product form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')  
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('edit_review', kwargs={
            'pk': self.boxreview.id}))
        self.assertEqual(response.status_code, 302)


class DeleteReviewTestCase(SetupModelTestCase):
    """
    Test delete review 
    """
    def test_edit_review_post_form_valid(self):
        """
        Test if user is authenticated and delete review
        """
        self.client.login(username='joe', password='12345')
        payload = {
           'review_text':'Review Text 3',
           'review_rating':'5',
        }
        response = reverse('delete_review', kwargs={
            'pk': self.boxreview.id})
        self.client.delete(response)

    def test_delete_review_wrong_user(self):
        """
        Test if user is authenticated and delete review
        """
        self.username = 'jim'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            email='jim@doe.com',
            password=self.password)
        self.client.login(username='jim', password='12345')
    
        response = self.client.get(reverse('delete_review', kwargs={
            'pk': self.boxreview.id}))
        self.client.delete(response)
        self.assertEqual(response.status_code, 302)


class DeleteBoxTestCase(SetupModelTestCase):
    """
    Test delete box 
    """
    def test_delete_box_post_form_valid(self):
        """
        Test if user is authenticated and delete box
        """
        self.client.login(username='joe', password='12345')
        response = reverse('delete_box', kwargs={
            'pk': self.boxtest.id})
        self.client.delete(response)

    def test_delete_box_not_staff_user(self):
        """
        Test if user is not staff and try to delete box
        """
        self.username = 'jim'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            email='jim@doe.com',
            password=self.password)
        self.user.is_staff = False 
        self.user.save()
        self.client.login(username='jim', password='12345')
    
        response = self.client.get(reverse('delete_box', kwargs={
            'pk': self.boxtest.id}))
        self.client.delete(response)
        self.assertEqual(response.status_code, 200)


class DeleteProductTestCase(SetupModelTestCase):
    """
    Test delete product 
    """
    def test_delete_product_post_form_valid(self):
        """
        Test if user is authenticated and delete product
        """
        self.client.login(username='joe', password='12345')
        response = reverse('delete_product', kwargs={
            'pk': self.producttest.id})
        self.client.delete(response)

    def test_delete_product_not_staff_user(self):
        """
        Test if user is not staff and try to delete product
        """
        self.username = 'jim'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            email='jim@doe.com',
            password=self.password)
        self.user.is_staff = False 
        self.user.save()
        self.client.login(username='jim', password='12345')
    
        response = self.client.get(reverse('delete_product', kwargs={
            'pk': self.producttest.id}))
        self.client.delete(response)
        self.assertEqual(response.status_code, 200)


class DeleteProductOnBoxTestCase(SetupModelTestCase):
    """
    Test delete product on box
    """
    def test_delete_product_on_box_post_form_valid(self):
        """
        Test if user is authenticated and delete product on box
        """
        self.client.login(username='joe', password='12345')
        response = reverse('deleteproductonbox', kwargs={
            'pk': self.productonboxtest.id})
        self.client.delete(response)

    def test_delete_product_on_box_not_staff_user(self):
        """
        Test if user is not staff and try to delete product on box
        """
        self.username = 'jim'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            email='jim@doe.com',
            password=self.password)
        self.user.is_staff = False 
        self.user.save()
        self.client.login(username='jim', password='12345')
    
        response = self.client.get(reverse('deleteproductonbox', kwargs={
            'pk': self.productonboxtest.id}))
        self.client.delete(response)
        self.assertEqual(response.status_code, 200)