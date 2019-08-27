from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'lend', views.LendFeedsViewSet)
router.register(r'borrow', views.BorrowFeedsViewSet)
router.register(r'all', views.MyFeedsViewSet)
router.register(r'report', views.ReportViewSet)
router.register(r'delete', views.DeleteMyFeed)
urlpatterns = router.urls
