from django.shortcuts import render


def store(request):
    context = {}
    return render(request, "MyApp/store.html", context)


def cart(request):
    context = {}
    return render(request, "MyApp/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "MyApp/checkout.html", context)


def login(request):
    context = {}
    return render(request, "MyApp/login.html", context)


def register(request):
    context = {}
    return render(request, "MyApp/register.html", context)
