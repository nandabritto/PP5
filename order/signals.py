""" System Module """
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()
