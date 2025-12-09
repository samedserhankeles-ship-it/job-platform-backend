from django.contrib import admin
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.views import JobViewSet, home 

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    
    path('api/v1/', include(router.urls)),
    
    # JWT Kimlik Doğrulama Uç Noktaları
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
