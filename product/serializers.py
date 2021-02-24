from rest_framework import serializers
from .models import *


class ProductSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductImageSerialiser(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ReviewSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
