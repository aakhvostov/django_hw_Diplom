from rest_framework import viewsets
from django_filters import rest_framework as filters
from product.permissions import IsAdminUserOrReadOnly
from .serializers import CollectionSerialiser, ProductInCollectionSerialiser
from .models import Collection


class CollectionViewSet(viewsets.ModelViewSet):
    """ Вьюсет для коллекций"""

    queryset = Collection.objects.all()
    serializer_class = CollectionSerialiser
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)


class ProductInCollectionViewSet(viewsets.ModelViewSet):
    """ Вьюсет для коллекций"""

    queryset = Collection.objects.all()
    serializer_class = ProductInCollectionSerialiser
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
