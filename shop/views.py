from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Service, Support
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    current_user = request.user.userprofile
    products = request.user.userprofile.product_list.all()
    print("Products of current User : " + str(products))
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'current_user': current_user})


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


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/service_detail.html',
                  {'service': service,
                   'cart_product_form': cart_product_form})


def service_page(request):
    services = Service.objects.all()

    return render(request, 'shop/product/services.html', {'services': services})


def service_purchased(request):
    current_user = request.user.userprofile
    print("Current User : " + str(current_user.conversion_rate))

    if current_user.conversion_rate == 0:
        current_user.conversion_rate = 1
        request.user.userprofile.save()
    print("Current User : " + str(current_user.conversion_rate))
    return render(request, 'shop/product/service_purchased.html', {})


def support_page(request):
    supports = Support.objects.all()

    return render(request, 'shop/product/support.html', {'supports': supports})
