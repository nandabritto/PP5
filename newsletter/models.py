from django.db import models

class NewsletterUser(models.Model):
    """
    Create newsletter model with email and date
    """
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
