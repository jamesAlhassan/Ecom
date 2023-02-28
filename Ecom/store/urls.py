from .views import StoreView, CartView, CheckoutView
from django.urls import path, include

urlpatterns = [
    path("", StoreView.as_view(), name='store'),
    path("cart/", CartView.as_view(), name='cart'),
    path("checkout/", CheckoutView.as_view(), name='checkout'),
]
