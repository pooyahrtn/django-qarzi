from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'lend', views.LendFeedsViewSet)
router.register(r'borrow', views.BorrowFeedsViewSet)

urlpatterns = router.urls
