from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Product, Review


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class ProductDetailSerialiser(serializers.ModelSerializer):
    """ Serializer для товара """

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')


class ProductShortSerialiser(serializers.ModelSerializer):
    """ Serializer для сериализатора отзывов """
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ReviewSerialiser(serializers.ModelSerializer):
    """ Serializer для отзывов к товарам """
    product = ProductShortSerialiser(many=False, read_only=True)
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'author', 'product', 'rating', 'created_at')

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении отзыва."""

        review = Review.objects.filter(author=self.context["request"].user)
        print(f'Review - {review}')
        if review.exists():
            raise ValidationError('Нельзя создавать больше одного отзыва')
        return data

