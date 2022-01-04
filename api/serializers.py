from rest_framework import serializers
from product.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    category = serializers.SlugRelatedField(many=False, slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
