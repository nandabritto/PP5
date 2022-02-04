from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.newsletter_signup, name='subscribe'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='unsubscribe'),
]
