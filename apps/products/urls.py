from django.urls import path
from .views import home, product_detail, category_products, search_products

urlpatterns = [
    path('', home, name='home'),
    path(
        'product/<slug:slug>/', product_detail, name='product_detail'
        ),
    path(
        'category/<slug:category_slug>/',
        category_products,
        name='category_products',
    ),
    path(
        'search/',
        search_products,
        name='search_products',
    ),
]