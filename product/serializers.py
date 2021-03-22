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


class ReviewListSerialiser(serializers.ModelSerializer):
    """ Serializer для просмотра отзывов к товарам """
    product = ProductShortSerialiser(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCUDSerialiser(serializers.ModelSerializer):
    """ Serializer для создания отзыво к товару """

    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        """
        Метод для валидации. Вызывается при создании и обновлении отзыва
        Проверка наличия более 1 отзыва к товару
        """

        product = Product.objects.get(id=self.context["request"].data['product'])
        review = Review.objects.filter(author=self.context["request"].user, product=product)
        if review.exists():
            raise ValidationError('Нельзя создавать больше одного отзыва к товару')
        return data

