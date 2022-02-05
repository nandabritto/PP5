from django.contrib import admin
from django.urls import path
from .views import newsletter_signup, newsletter_unsubscribe, send_newsletter

urlpatterns = [
    path('subscribe/', views.newsletter_signup, name='subscribe'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='unsubscribe'),
    path('send_newsletter/', views.send_newsletter, name='send_newsletter'),
]
