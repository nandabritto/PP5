""" System Module """
from django.contrib import admin
from django.urls import path
from . import views
from .views import CheckoutView, PaymentView

urlpatterns = [
    path('', views.order, name='order'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),
]
