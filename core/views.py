from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsOwnerOrReadOnly 

def home(request):
    return render(request, 'home.html') 

class JobViewSet(viewsets.ModelViewSet):
    # Performans düzeltmesi: select_related('user') ile N+1 sorgu çözüldü
    queryset = Job.objects.all().select_related('user')
    
    serializer_class = JobSerializer
    
    # Güvenlik düzeltmesi: Yetkilendirme kuralı uygulandı
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

    # Güvenlik düzeltmesi: Oluşturucu user alanını otomatik atar
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
