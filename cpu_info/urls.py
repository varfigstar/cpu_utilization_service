from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CpuInfoSliceViewSet

router = DefaultRouter()
router.register(r'cpu_info', CpuInfoSliceViewSet, basename="cpu_info")

urlpatterns = [
    path('', include(router.urls))
]
