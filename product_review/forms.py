""" System Module """
from django import forms
from .models import BoxReview


class AddReviewForm(forms.ModelForm):
    """
    Creates Add review form
    """
    class Meta:
        model = BoxReview
        fields = ('review_text','review_rating')
