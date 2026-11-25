from django.shortcuts import render
from django.db.models import Q, F
from .models import Product

def index(request):
    products_price_quantity = Product.objects.filter(Q(price__gt = 50) | Q(quantity__lt = 10))
    products_name_price = Product.objects.filter(Q(name__contains = "phone" & Q(price__gt = 50) | Q(price__range = (100, 500))))
    products_not = Product.objects.filter(~Q(price__lt = 200))
    update_price = Product.objects.update(price=F('price') + 10)
    products_quantity = Product.objects.filter(price__gt=F('quantity'))
    products_update_quantity = Product.objects.update(quantity=F('quantity') + 1)

    context = {
        'products_price_quantity': products_price_quantity,
        'products_name_price': products_name_price,
        'products_not': products_not,
        'update_price': update_price,
        'products_quantity': products_quantity,
        'products_update_quantity': products_update_quantity,

    }

    return render(request, 'store/index.html', context)
