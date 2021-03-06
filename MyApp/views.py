from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegisterForm
import datetime
from django.core.exceptions import PermissionDenied


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wait")
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "MyApp/register.html", context)


@login_required
def store(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "MyApp/store.html", context)


@login_required
def cart(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "MyApp/cart.html", context)


@login_required
def checkout(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "MyApp/checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    # print("Action:", action)
    # print("Product:", productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("item was added", safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = transaction_id
        order.complete = True
        order.save()
    return JsonResponse("Payment Complete", safe=False)


@login_required
def viewOrders(request):
    if request.user.is_authenticated:
        orders = request.user.customer.order_set.all()
    context = {"orders": orders}
    return render(request, "MyApp/orders.html", context=context)


@login_required
def orderDetails(request, pk):
    order = Order.objects.get(id=pk)
    items = order.orderitem_set.all()
    context = {"items": items}
    if str(request.user) == str(order.customer):
        return render(request, "MyApp/order_details.html", context=context)
    else:
        raise PermissionDenied


def wait(request):
    return render(request, "MyApp/wait.html")
    