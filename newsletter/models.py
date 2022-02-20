""" System Module """
from django.db import models


class NewsletterUser(models.Model):
    """
    Create newsletter model with email and date
    """
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class Newsletter(models.Model):
    """
    Permit send newletter from admin to users
    """
    subject = models.CharField(max_length=250)
    body = models.TextField()
    email = models.ManyToManyField(NewsletterUser)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.subject)
