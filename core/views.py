from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsOwnerOrReadOnly # Yeni izin dosyamızı import ettik

# (Bu fonksiyon API için gerekli değildir, HTML sayfası sunuyorsa kalabilir)
def home(request):
    return render(request, 'home.html') 

class JobViewSet(viewsets.ModelViewSet):
    # Performans düzeltmesi: select_related('user') ile N+1 sorgu çözüldü
    queryset = Job.objects.all().select_related('user')
    
    serializer_class = JobSerializer
    
    # Güvenlik düzeltmesi: Okuma herkese açık, yazma/düzenleme/silme sahibine ait
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

    # Güvenlik düzeltmesi: İlan oluşturulurken user alanı otomatik atanır
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
