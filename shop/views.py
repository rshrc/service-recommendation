from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Service
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def service_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    services = Service.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        services = services.filter(category=category)
    return render(request,
                  'shop/services/list.html',
                  {'category': category,
                   'categories': categories,
                   'services': services})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def service_detail(request, id, slug):
    service = get_object_or_404(Service,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'shop/services/detail.html', {'service': service})
