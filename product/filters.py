from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
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


class MixedPermission:
    """Миксин permissions для action"""

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class NewViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 MixedPermission,
                 GenericViewSet):
    """
        A viewset that provides default `create()`, `retrieve()`, `update()`,
        `partial_update()`, `destroy()` and `list()` actions.
        """
    pass
