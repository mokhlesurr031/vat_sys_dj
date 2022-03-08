from rest_framework import serializers
from .models import HSCode, ProductVariant, Product


class HSCodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = HSCode
        fields = '__all__'


class ProductVariantSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



