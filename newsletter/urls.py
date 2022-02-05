from django.contrib import admin
from django.urls import path
from .views import NewsletterList
from . import views

urlpatterns = [
    path('subscribe/', views.newsletter_signup, name='subscribe'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='unsubscribe'),
    path('send/', views.send_newsletter, name='send'),
    path('list', NewsletterList.as_view(), name="newsletters"),
]
