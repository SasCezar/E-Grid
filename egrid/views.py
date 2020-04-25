from django.http import HttpResponse
from django.shortcuts import render
from egrid.models import Product, Order, AdministrativeOrganization


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)


def order(request, pk):
    order = Order.objects.get(pk=pk)
    product = Product.objects.get(id=order.product_id_id)
    buyer = AdministrativeOrganization.objects.get(id=order.buyer_id_id)
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


def addUser():
    # Create user and save to the database
    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

    # Update fields and then save again
    user.first_name = 'John'
    user.last_name = 'Citizen'
    user.save()
    return HttpResponse("saved")


def product(request, pk):
    product = Product.objects.get(id=pk)
    orders = Order.objects.filter(product_id_id=pk)
    context = {"orders": orders, "product": product}
    return render(request, 'product.html', context)
