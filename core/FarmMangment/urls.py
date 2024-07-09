from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, CropViewSet, AnimalViewSet

router = DefaultRouter()
router.register('farms', FarmViewSet)
router.register('crops', CropViewSet)
router.register('animals', AnimalViewSet)

urlpatterns = router.urls
