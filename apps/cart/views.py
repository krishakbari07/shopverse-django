from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from apps.products.models import Product

# Create your views here.

# @login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


# @login_required
def cart_detail(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = sum(
        item.total_price
        for item in cart_items
    )

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return render(
        request,
        'cart/cart_detail.html',
        context,
    )


def increase_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_detail')


def decrease_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart_detail')


def remove_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    cart_item.delete()

    return redirect('cart_detail')
