from rest_framework import viewsets
from django_filters import rest_framework as filters

from .serializers import ProductDetailSerialiser, ReviewCUDSerialiser, ReviewListSerialiser
from .permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrAdmin
from .filters import ProductFilter, ReviewFilter
from .models import Product, Review


class ProductViewSet(viewsets.ModelViewSet):
    """ Вьюсет для товаров"""

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerialiser
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class ReviewViewSet(viewsets.ModelViewSet):
    """ Вьюсет для отзывов к товарам"""

    queryset = Review.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReviewFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAdminUserOrReadOnly]
        else:
            permission_classes = [IsReviewAuthorOrAdmin]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerialiser
        return ReviewCUDSerialiser
