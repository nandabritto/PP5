""" System Module """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_countries.fields import CountryField

class UserProfile(models.Model):
    """
    Create user profile with dfaul info
    """
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    default_address1 = models.CharField(max_length=100, null=True, blank=True)
    default_address2 = models.CharField(max_length=100, null=True, blank=True)
    default_county = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(multiple=False, null=True, blank=True)
    default_eircode = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        """
        Return string
        """
        return self.customer.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(customer=instance)
    instance.userprofile.save()

