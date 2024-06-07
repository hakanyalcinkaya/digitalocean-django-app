from django.shortcuts import render
from product.models import Product

def index(request):
    products = Product.objects.all()
    context = dict(
        products=products
    )
    return render(request, "index.html", context)
