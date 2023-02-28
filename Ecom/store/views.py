from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class StoreView(TemplateView):
    template_name = 'store.html'


class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'