""" System Module """
from django.urls import path
from . import views
from .views import ListBoxes, ListProducts, ListProductsOnBox

urlpatterns = [
    path('', views.boxes, name='boxes'),
    path("box_details/<int:pk>/",
         views.box_detail, name="box_details"),
    path("product_details/<int:pk>/",
         views.product_detail, name="product_details"),
    path('add_box/', views.add_box, name='add_box'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_product_box/', views.add_product_on_boxes, name='add_product_box'),
    path('editbox/<int:pk>/', views.edit_box, name='edit_box'),
    path('deletebox/<int:pk>/', views.delete_box, name='delete_box'),
    path('editproduct/<int:pk>/', views.edit_product, name='edit_product'),
    path('editproductonbox/<int:pk>/', views.edit_product_on_box, name='editproductonbox'),
    path('deleteproduct/<int:pk>/', views.delete_product,name='delete_product'),
    path('deleteproductonbox/<int:pk>/', views.delete_productonbox,name='deleteproductonbox'),
    path('boxes_list/', ListBoxes.as_view(), name='boxes_list'),
    path('products_list/', ListProducts.as_view(), name='products_list'),
    path('productsonbox_list/', ListProductsOnBox.as_view(), name='productsonbox_list'),

]

