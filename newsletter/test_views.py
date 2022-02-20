""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Newsletter, NewsletterUser


class SetupModelTestCase(TestCase):
    """
    Base test case to be used in all models tests
    """
    def setUp(self):
        self.user = User.objects.create_user('joe', 'joe@example.com', '12345')
        self.user.is_staff = True
        self.user.save()
        self.client.login(username='joe', password='12345')
        self.newsletter_user = NewsletterUser.objects.create(
            email='email@email.com'
        )
        self.newsletter = Newsletter.objects.create(
            subject='subject',
            body='body',
        )


class NewsletterSignUpTestCase(SetupModelTestCase):
    """
    Test newsletter sign up page and features
    """
    def test_newsletter_signup_post_email_exist(self):
        """
        Test newsletter sign up if email already exist in db
        """
        payload = {
           'email': 'email@email.com',
        }
        response = self.client.post(reverse('subscribe'), payload)
        self.assertEqual(response.status_code, 302)

    def test_newsletter_signup_post_email_dont_exist(self):
        """
        Test newsletter sign up if email don't exist in db
        """
        payload = {
           'email': 'email2@email.com',
        }
        response = self.client.post(reverse('subscribe'), payload)
        self.assertEqual(response.status_code, 302)

    def test_get_newsletter_form(self):
        """
        Test newsletter sign up form
        """
        response = self.client.get(reverse('subscribe'))
        self.assertEqual(response.status_code, 200)


class NewsletterUnsubscribeTestCase(SetupModelTestCase):
    """
    Test newsletter unsubscribe page and feature
    """
    def test_newsletter_unsubscribe_post_email_exist(self):
        """
        Test newsletter unsubscribe if email already exist in db
        """
        payload = {
           'email': 'email@email.com',
        }
        response = self.client.post(reverse('unsubscribe'), payload)
        self.assertEqual(response.status_code, 302)

    def test_newsletter_unsubscribe_post_email_dont_exist(self):
        """
        Test newsletter unsubscribe if email dont exist in db
        """
        payload = {
           'email': 'email3@email.com',
        }
        response = self.client.post(reverse('unsubscribe'), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_newsletter_form(self):
        """
        Test newsletter unsubscribe form
        """
        response = self.client.get(reverse('unsubscribe'))
        self.assertEqual(response.status_code, 200)


class SendNewsletterTestCase(SetupModelTestCase):
    """
    Test send newsletter page
    """
    def test_send_newsletter_post(self):
        """
        Test send newsletter feature
        """
        payload = {
            'subject': 'subject',
            'body': 'body',
            'email': self.newsletter_user.id,
        }
        response = self.client.post(reverse('send'), payload)
        self.assertEqual(response.status_code, 302)

    def test_send_newsletter_post_invalid(self):
        """
        Test send newsletter feature when post is invalid
        """
        payload = {
            'subject': '',
            'body': 'body',
            'email': self.newsletter_user.id,
        }
        response = self.client.post(reverse('send'), payload)
        self.assertEqual(response.status_code, 200)

    def test_get_newslettercreation_form(self):
        """
        Test newsletter newslettercreation form
        """
        response = self.client.get(reverse('send'))
        self.assertEqual(response.status_code, 200)

    def test_get_newslettercreation_form_customer_user(self):
        """
        Test newsletter newslettercreation form as customer user
        """
        self.user = User.objects.create_user('jim', 'jim@example.com', '12345')
        self.client.login(username='jim', password='12345')
        response = self.client.get(reverse('send'))
        self.assertEqual(response.status_code, 200)
