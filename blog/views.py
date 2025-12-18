from django.shortcuts import render
from .models import Product


def index_page(request):
    context = {'name': 'ali akbari'}
    return render(request, 'blog/index.html', context)

def store_page(request):
    products = Product.objects.all()
    if products:
        context = {
            'products': products
        }
    else:
        context = {}
    return render(request, 'blog/store.html', context)

def card_page(request):
    return render(request, 'blog/card.html', {})

def about_us_page(request):
    return render(request, 'blog/about-us.html', {})

def contact_us_page(request):
    return render(request, 'blog/contact-us.html', {})
