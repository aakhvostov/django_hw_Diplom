from .views import CollectionViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/v1/product-collections', CollectionViewSet, basename="collections")
urlpatterns = []
