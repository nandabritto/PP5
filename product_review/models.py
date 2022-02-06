from django.db import models
from .products.models import Box

RATING=(
    ('1', '1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
)

class ProductReview(models.Model):
    """"
    Creates box review
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.CharField(choices=RATING)

    def get_review_rating(self):
        return self.review_rating