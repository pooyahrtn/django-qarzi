from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

V_ONE = [
    path(r'users/', include('users.urls')),
    path(r'feeds/', include('feeds.urls'))
]

urlpatterns = [
    path('api/v1/', include(V_ONE)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
