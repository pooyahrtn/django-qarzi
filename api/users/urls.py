from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import UserViewSet, UserCreateViewSet, TokenObtainView

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'', UserCreateViewSet)

urlpatterns = [
    path('token/',
         TokenObtainView.as_view(),
         name='token_obtain_pair'
         ),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'
         ),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
