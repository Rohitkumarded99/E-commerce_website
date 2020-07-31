from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("shirt/", views.shirt, name="shirt"),
    path("Tshirt/", views.Tshirt, name="Tshirt"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("search", views.search, name="search"),
    path("products/<int:myid>", views.productview, name="productview"),
    path("checkout", views.checkout, name="checkout"),
    path("handlerequest/", views.handlerequest, name="handlerequest"),
    path("paymentsquery/", views.paymentsquery, name="paymentsquery"),
    path("cancelation/", views.cancelation, name="cancelation"),
    path("Terms/", views.Terms, name="Terms"),

]
