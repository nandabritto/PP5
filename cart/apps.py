""" System Module """
from django.apps import AppConfig


class CartConfig(AppConfig):
    """
    Cart config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
