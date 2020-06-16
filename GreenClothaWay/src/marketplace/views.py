import datetime

from django.shortcuts import render
from inseration.models import Inseration

from inseration.forms import InserationFilterForm


def index_view(request):
    test = "hello"
    year = datetime.datetime.now().year
    return render(request, 'marketplace/index.html', locals())


def marketplace_view(request):
    year = datetime.datetime.now().year
    inseration_list = []

    if request.method == 'POST':
        form = InserationFilterForm(request.POST)
        form.save(commit=False)
        category = form.cleaned_data['category']
        subcategory = form.cleaned_data['subcategory']
        size = form.cleaned_data['size']
        print(category)

        #TODO leeres form behandeln

        inseration_list = Inseration.objects.filter(category=category, subcategory=subcategory, size=size)

    # category_list = ['Unisex', 'Women', 'Men']
    #  subcategory_list = ['T-Shirt', 'Hoodie', 'Polo', 'Jeans', 'Shorts', 'Sneaker', 'Longsleeve', 'Sweatpants', 'Accesoires',
    # #                     'Hats', 'Jacket']
    # size_list = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44',
    #           '45', '46', '47', '48']
    else:
        form = InserationFilterForm()
        inseration_list = Inseration.objects.order_by('-modified_at')

    context = {'inseration_list': inseration_list,
               'filter_form': form,
               'locals': locals()}

    return render(request, 'marketplace/product-page.html', context)


def about_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/about-us.html', locals())


def cart_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/shopping-cart.html', locals())
