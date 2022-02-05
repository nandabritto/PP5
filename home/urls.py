from django.contrib import admin
from django.urls import path
from .views import Management
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('management/', Management.as_view(), name='management'),
]
