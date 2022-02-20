""" System Mdodule """
from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """
    User profile admin config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
