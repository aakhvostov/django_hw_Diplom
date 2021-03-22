from rest_framework import routers
from .views import OrderViewSet


router = routers.DefaultRouter()
router.register(r'api/v1/orders', OrderViewSet, basename='orders')
urlpatterns = []
