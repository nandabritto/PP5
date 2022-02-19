""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Newsletter, NewsletterUser
from .views import send_newsletter



class SetupModelTestCase(TestCase):
    """
    Base test case to be used in all models tests
    """
    def setUp(self):
        self.user = User.objects.create_user('joe', 'joe@example.com', '12345')  
        self.user.is_staff = True 
        self.user.save()
        self.client.login(username='joe', password='12345')
        self.nlu = NewsletterUser.objects.create(
            email='email@email.com'
        )
        self.nl = Newsletter.objects.create(
            subject='subjet',
            body='body',
        )

class SendNewsletterTestCase(SetupModelTestCase):
    def test_send_newsletter_post(self):
        payload = {
            'subject':'subjet',
            'body':'body',
            'email':self.nlu.id,
        }
        response = self.client.post(reverse('send'), payload)
        self.assertEqual(response.status_code, 302)

 