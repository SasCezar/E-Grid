from django.http import HttpResponse
from django.shortcuts import render
from egrid.models import Product, Order


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)


def order(request, pk):
    order = Order.objects.get(pk=pk)
    context = {"order": order}
    return render(request, 'order.html', context)






def about_us(request):
    return render(request,'about_us.html')

