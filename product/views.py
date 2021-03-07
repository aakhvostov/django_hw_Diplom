from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Product, Review
from .serializers import ProductDetailSerialiser, ReviewSerialiser
from .permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrAdmin
from .filters import ProductFilter, ReviewFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerialiser
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialiser
    # permission_classes = [IsReviewAuthorOrAdmin]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReviewFilter

