from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "MyApp/store.html", context)


def cart(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {"get_cart_total": 0, "get_cart_items": 0}
    context = {"items": items, "order": order}
    return render(request, "MyApp/cart.html", context)


def checkout(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {"get_cart_total": 0, "get_cart_items": 0}
    context = {"items": items, "order": order}
    return render(request, "MyApp/checkout.html", context)


def login(request):
    context = {}
    return render(request, "MyApp/login.html", context)


def register(request):
    context = {}
    return render(request, "MyApp/register.html", context)
