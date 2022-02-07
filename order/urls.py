""" System Module """
from django.urls import path
from . import views
from .views import CheckoutView, PaymentView

urlpatterns = [
    # path('', views.order, name='order'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('checkout_summary', views.checkout_summary, name='checkout_summary'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('success/<pk>', views.success, name='success'),
]
