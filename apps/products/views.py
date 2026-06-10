from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
# Create your views here.


def home(request):

    products = Product.objects.filter(is_available=True)

    context = {
        'products': products,
    }

    return render(
        request,
        'products/home.html',
        context,
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)

    return render(
        request,
        'products/product_detail.html',
        {'product': product},
    )


def category_products(request, category_slug):

    category = get_object_or_404(
        Category,
        slug=category_slug
    )

    products = Product.objects.filter(
        category=category,
        is_available=True
    )

    return render(
        request,
        'products/category_products.html',
        {
            'category': category,
            'products': products
        }
    )


def search_products(request):
    query = request.GET.get('q')

    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query),
        is_available=True,
    )

    return render(
        request,
        'products/search_results.html',
        {'products': products, 'query': query},
    )
