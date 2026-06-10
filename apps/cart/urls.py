from django.urls import path
from .views import add_to_cart, cart_detail, remove_cart, increase_cart, decrease_cart

urlpatterns = [
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("", cart_detail, name="cart_detail"),
    path("increase/<int:cart_id>/", increase_cart, name="increase_cart"),
    path("decrease/<int:cart_id>/", decrease_cart, name="decrease_cart"),
    path("remove/<int:cart_id>/", remove_cart, name="remove_cart"),
]
