from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Job
from .serializers import JobSerializer

def home(request):
    return render(request, 'home.html')

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
