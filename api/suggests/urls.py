from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'income', views.IncomeSuggestsViewSet)
router.register(r'outcome', views.OutcomeSuggestsViewSet)
router.register(r'suggest_borrow', views.CreateBorrowSuggestViewSet)
router.register(r'suggest_lend', views.CreateLendSuggestViewSet)

urlpatterns = router.urls
