from django_filters import rest_framework as filters
from .models import Order


class OrderFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            'status': ['exact'],
            'total_price': ['lt', 'gt', 'range', 'exact'],
            'created_at': ['lt', 'gt', 'range', 'exact'],
            'updated_at': ['lt', 'gt', 'range', 'exact'],
        }
