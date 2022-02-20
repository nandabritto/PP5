""" System Module """
from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    """
    Newsletter app config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'
