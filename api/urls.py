from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='Routes'),
    path('products', views.products_view, name='Products'),
    path('products/<str:category>', views.filtered_product_view, name='Product'),
    path('categories', views.categories_view, name='Category'),
]
