import datetime

from django.shortcuts import render
from inserations.models import Inseration


def index_view(request):
    test = "hello"
    year = datetime.datetime.now().year
    return render(request, 'marketplace/index.html', locals())


def marketplace_view(request):
    year = datetime.datetime.now().year
    inseration_list = Inseration.objects.order_by('-modified_at')
    return render(request, 'marketplace/product-page.html', {locals(), inseration_list})


def about_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/about-us.html', locals())


def cart_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/shopping-cart.html', locals())
