from django_filters import rest_framework as filters
from .models import Product, Review


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['lt', 'gt', 'range'],
            'description': ['icontains'],
        }


class ReviewFilter(filters.FilterSet):
    author_id = ''
    product_id = ''

    class Meta:
        model = Review
        fields = {
            'created_at': ['lt', 'gt', 'range', 'exact'],
            'author_id': ['exact'],
            'product_id': ['exact'],
        }
