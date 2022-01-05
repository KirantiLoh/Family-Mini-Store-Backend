from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from product.models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = {
        'products',
        'products/<str:category>',
        'categroies'
    }
    return Response(routes)

@api_view(['GET'])
def products_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_result(request, name):
    products = Product.objects.filter(name__icontains = name)
    if products.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'message':"Produk yang anda cari tak ada"}, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filtered_product_view(request, category):
    try:
        category = Category.objects.get(slug=category)
        product = Product.objects.filter(category=category)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({'message':"Tak ada kategori itu"}, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def categories_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)    
