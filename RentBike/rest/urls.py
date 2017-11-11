from rest_framework import routers
from .views import ShopViewSet


router = routers.DefaultRouter()
router.register(r'shops', ShopViewSet)

urlpatterns = router.urls