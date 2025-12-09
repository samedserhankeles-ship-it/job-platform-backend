# core/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Sadece objenin sahibi yazma (PUT, PATCH, DELETE) iznine sahiptir.
    Okuma (GET) herkese açıktır.
    """
    
    def has_object_permission(self, request, view, obj):
        # Güvenli metotlar (GET, HEAD, OPTIONS) okuma işlemleridir ve herkese izin verilir.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Diğer metotlar (PUT, PATCH, DELETE) yazma işlemleridir.
        # Bu izin, isteği yapan kullanıcının (request.user) objenin (Job ilanı) sahibi (obj.user) olup olmadığını kontrol eder.
        return obj.user == request.user
