from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return render(request, 'blog/index.html', {})

def store_page(request):
    return render(request, 'blog/index.html', {})

def card_page(request):
    return render(request, 'blog/index.html', {})

def about_us_page(request):
    return HttpResponse('this is a about us')

def contact_us_page(request):
    return HttpResponse('this is contact us')

