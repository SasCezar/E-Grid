from django.http import HttpResponse
from django.shortcuts import render
from egrid.models import Product, Order


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)



