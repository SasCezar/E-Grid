from django.http import HttpResponse
from django.shortcuts import render
from egrid.models import Product, Order, AdministrativeOrganization


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)


def order(request, pk=1):
    order = Order.objects.get(pk=1)
    product = Product.objects.get(id=order.product_id_id)
    buyer = AdministrativeOrganization.objects.get(id=order.buyer_id_id)
    context = {"order": order,"product":product,"buyer":buyer}
    return render(request, 'order.html', context)


def about_us(request):
    return render(request,'about_us.html')

