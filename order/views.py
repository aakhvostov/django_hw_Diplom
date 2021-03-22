from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializers import OrderSerialiser
from .permissions import IsOrderOwner, OrderStatusChange
from .filters import OrderFilter
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    """ Вьюсет для заказов"""

    queryset = Order.objects.all()
    serializer_class = OrderSerialiser
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_permissions(self):
        """
        Права доступа для изменения статуса заказа
        """
        if self.action == 'partial_update' or self.action == 'update':
            permission_classes = [OrderStatusChange]
        else:
            permission_classes = [IsOrderOwner]
        return [permission() for permission in permission_classes]
