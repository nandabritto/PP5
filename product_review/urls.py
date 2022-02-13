""" System Module """
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("edit_review/<int:pk>/", views.edit_review, name="edit_review"),
]