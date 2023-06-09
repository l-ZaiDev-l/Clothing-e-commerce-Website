from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.About, name="About"),
    path("products_page", views.products_page, name="products_page"),
    path("product/<int:product_id>/", views.product_page, name="product_page"),
    path("cart", views.cart, name="cart"),
    path("login", views.user_login, name="login"),
    path("payment", views.payment, name="payment"),
    path("update_item/", views.updateItem, name="update_item"),
    path("Men_products/", views.Men_products, name="Men_products"),
    path("Women_products/", views.Women_products, name="Women_products"),
    path("Chemise_products/", views.Chemise_products, name="Chemise_products"),
    path("Tshirt_products/", views.Tshirt_products, name="Tshirt_products"),
    path("Pyjama_products/", views.Pyjama_products, name="Pyjama_products"),
]
