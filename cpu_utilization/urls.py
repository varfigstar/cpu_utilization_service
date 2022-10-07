from django.contrib import admin
from django.urls import path, include

api_patterns = [
    path("", include("cpu_info.urls"))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("cpu_info.urls")),
]
