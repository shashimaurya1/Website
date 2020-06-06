import datetime

from django.shortcuts import render


def index_view(request):
    test = "hello"
    year = datetime.datetime.now().year
    return render(request, 'marketplace/index.html', locals())


def marketplace_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/product-page.html', locals())


def about_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/about-us.html', locals())


def cart_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/shopping-cart.html', locals())
