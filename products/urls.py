from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path("product_details/<int:pk>", views.product_detail, name="product_details")
   
]
