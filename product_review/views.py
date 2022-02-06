from django.shortcuts import render
from .models import BoxReview
from .forms import AddReviewForm

def add_review(request):
    """
    Creates a view for user reviews
    """
    form = AddReviewForm

    context = {
        'form': form
        }
    reviews = BoxReview.objects.all()
    return render(request, 'product_review/reviews.html',context)
