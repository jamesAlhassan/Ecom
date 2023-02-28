from .models import Product
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.
class StoreView(ListView):
    model = Product
    template_name = 'store.html'


class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'