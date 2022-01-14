from django.db import models
from django.contrib.auth.models import User 


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transactional_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    