"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 1. Kendi uygulamalarınızdan view'ları import edin.
from core.views import JobViewSet, home 

# 2. Router oluşturun (viewset'ler için gerekli)
router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    # Ana dizin ("/") isteğini core/views.py'deki home fonksiyonuna yönlendirir.
    path('', home, name='home'), 
    
    # Django Admin paneli
    path('admin/', admin.site.urls),
    
    # 3. Kendi API uç noktalarınızı router ile ekleyin
    path('api/v1/', include(router.urls)),
    
    # 4. JWT Kimlik Doğrulama Uç Noktaları (Giriş ve Token Yenileme)
    # Token almak için: /api/v1/auth/token/
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Token yenilemek için: /api/v1/auth/token/refresh/
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Opsiyonel: Diğer uygulamalarınızın URL'lerini buraya ekleyebilirsiniz (örneğin: path('api/v1/users/', include('users.urls')))
]
