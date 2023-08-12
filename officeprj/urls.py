
from django.contrib import admin
from django.urls import path
from shop.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',home),
    path('shop/<esm>',information),
]
