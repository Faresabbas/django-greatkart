from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product


def store(request, slug=None):
    categories = None
    products = None

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()
    context = {'products': products,
               'products_count': products_count}
    return render(request, 'store/store.html', context)


def product_detail(request, slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=slug, product_slug=product_slug)
    except Exception as e:
        raise e

    context = {'single_product': single_product}
    return render(request, 'store/product_detail.html', context)
