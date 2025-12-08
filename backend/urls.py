"""
URL configuration for job-platform backend.
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("health/", views.health_check, name="health_check"),
    path("admin/", admin.site.urls),
]
