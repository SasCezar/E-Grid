from django.http import HttpResponse
from django.shortcuts import render
from egrid.models import Product, Order, Organization


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)


def order(request, pk):
    order = Order.objects.get(pk=pk)
    product = Product.objects.get(id=order.product_id_id)
    buyer = Organization.objects.get(id=order.buyer_id_id)
    context = {"order": order, "product": product, "buyer": buyer}
    return render(request, 'order.html', context)


def about_us(request):
    return render(request, 'about_us.html')


def maps(request):
    pk = 1
    print(Order.objects.get(id=pk).buyer_id.name)
    return render(request, 'maps.html')


def login(request):
    return render(request, 'login.html')
