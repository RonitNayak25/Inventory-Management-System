from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", store, name="store"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("update_item/", updateItem, name="update_item"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="MyApp/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="MyApp/logout.html"), name="logout"
    ),
    path("process_order/", processOrder, name="process_order"),
]
