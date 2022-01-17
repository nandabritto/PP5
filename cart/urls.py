""" System Module """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('update_cart/', views.updateCart, name='update_cart'),
]
