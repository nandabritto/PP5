""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from .models import NewsletterUser, Newsletter


class SetupModelTestCase(TestCase):
    """
    Base test case to be used in all models tests
    """
    def setUp(self):
        """ Setup for testing models """        
        self.email = 'joe@email.com'
        self.subject = 'Test Subject'
        self.body = 'Test Body'
        self.status = 'Published'     
        self.nlu = NewsletterUser.objects.create(email=self.email)


class NewsletterUserTestCase(SetupModelTestCase):
    """
    Test NewsletterUser model function
    """
    def test__str__(self):
        """
        Test if newsletter user is returning correct string
        """
        self.assertEqual(str(self.nlu),'joe@email.com')


class NewsletterTestCase(SetupModelTestCase):
    """
    Test Newsletter model function
    """
    def test__str__(self):
        """
        Test if newsletter  is returning correct string
        """
        news = Newsletter.objects.create(
            subject=self.subject,
            body=self.body,
            status=self.status)

        self.assertEqual(str(news), 'Test Subject')