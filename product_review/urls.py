""" System Module """
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('my_review/', views.my_review, name='my_review'),
]