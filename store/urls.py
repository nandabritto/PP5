"""
System Module
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('profile/', include('user_profile.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('review/', include('product_review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
