from django_filters import rest_framework as filters
from .models import *


class OrderFilter(filters.FilterSet):
    products = ProductInOrder.objects.filter(order=order)

    class Meta:
        model = Order
        fields = {
            'status': ['exact'],
            'total_price': ['lt', 'gt', 'range', 'exact'],
            'created_at': ['lt', 'gt', 'range', 'exact'],
            'updated_at': ['lt', 'gt', 'range', 'exact'],
        }
