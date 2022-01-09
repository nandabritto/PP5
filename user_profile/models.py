from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField

class User_Profile(models.Model):
    """
    User profile model for store all user preferences
    """
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField()
    street_adress = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=20, null=True, blank=False)
    postcode = models.CharField(max_length=5, null=True, blank=True)
    country = CountryField(blank_label='Country *', null= True, blank=True)
    

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(profile_user=instance)
    instance.userprofile.save()




