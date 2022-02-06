from django.shortcuts import render
from .models import BoxReview

def my_review(request):
    """
    Creates a view for user reviews
    """
    reviews = BoxReview.objects.filter(customer=request.user).order_by('-id')
    return render(request, 'product_review/reviews.html',{'reviews':reviews})
