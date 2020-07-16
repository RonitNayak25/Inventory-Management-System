from django.urls import path
from .views import *

urlpatterns = [
    path("", store, name="store"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
]
