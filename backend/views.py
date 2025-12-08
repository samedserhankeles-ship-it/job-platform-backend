"""
Views for the job-platform backend.
"""

from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    """
    Home page view with information about the backend and Speed Insights setup.
    """
    return render(request, "home.html")


def health_check(request):
    """
    Health check endpoint for monitoring.
    """
    return JsonResponse({
        "status": "healthy",
        "service": "job-platform-backend",
        "version": "1.0.0",
    })
