""" System Module """
from django.urls import path
from . import views
from .views import ListProducts

urlpatterns = [
    path('', views.boxes, name='boxes'),
    path("product_details/<int:pk>/",
         views.product_detail, name="product_details"),
    path('add_box/', views.add_box, name='add_box'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('boxes_list/', ListProducts.as_view(), name='boxes_list'),
]

