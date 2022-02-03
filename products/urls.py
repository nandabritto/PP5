""" System Module """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.boxes, name='boxes'),
    path("product_details/<int:pk>",
         views.product_detail, name="product_details"),
    path('add', views.add_product, name='add_product'),
    path('edit/<int:pk>', views.edit_product, name='edit_product'),
]

