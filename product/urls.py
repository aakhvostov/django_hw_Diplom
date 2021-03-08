from rest_framework import routers
from .views import ProductViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register(r'api/v1/products', ProductViewSet)
router.register(r'api/v1/product-reviews', ReviewViewSet)
urlpatterns = []
