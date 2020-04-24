from django.http import HttpResponse
from django.shortcuts import render
from egrid.models import Product, Order


# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    context = {"products": products}
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")


# def request_detail(request, pk):
#     detail = Order.objects.get(pk=pk)
#     context = {"detail": detail}
#     return render(request, "detail.html", context)
