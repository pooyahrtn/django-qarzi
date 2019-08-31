from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
import os

V_ONE = [
    path(r'users/', include('users.urls')),
    path(r'feeds/', include('feeds.urls')),
    path(r'suggests/', include('suggests.urls')),
]


urlpatterns = [
                  path('api/v1/', include(V_ONE)),
                  path(os.getenv('DJANGO_ADMIN_URL'), admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
