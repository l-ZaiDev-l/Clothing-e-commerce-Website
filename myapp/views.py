from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render, get_object_or_404
from .models import *

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "pages/index.html", context)


# def profile(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []
#         order = {"get_cart_total": 0, "get_cart_items": 0}
#         cartItems = order["get_cart_items"]
#     products = Product.objects.all()
#     context = {"cartItems": cartItems, "customer": customer}
#     return render(request, "pages/Profile.html", context)


def profile(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        if request.method == "POST":
            form = ProfileImageForm(request.POST, request.FILES, instance=customer)
            if form.is_valid():
                form.save()
        else:
            form = ProfileImageForm(instance=customer)

    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]

    products = Product.objects.all()
    context = {
        "cartItems": cartItems,
        "customer": customer,
        "form": form,  # Add the form to the context
    }
    return render(request, "pages/Profile.html", context)


def About(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"cartItems": cartItems}
    return render(request, "pages/About.html", context)


def products_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "pages/products_page.html", context)


def product_page(request, product_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]

    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product, "cartItems": cartItems}
    context["images"] = product.productimage_set.all()
    return render(request, "pages/product_page.html", context)


def Men_products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.filter(gender="Men")
    context = {"products": products, "cartItems": cartItems}
    return render(request, "pages/Men_products.html", context)


def Women_products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.filter(gender="Women")
    context = {"products": products, "cartItems": cartItems}
    return render(request, "pages/Women_products.html", context)


def Chemise_products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.filter(type="Chemise")
    context = {"products": products, "cartItems": cartItems}
    return render(request, "pages/Chemise_products.html", context)


def Tshirt_products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.filter(type="T-shirt")
    context = {"products": products, "cartItems": cartItems}
    return render(request, "pages/Tshirt_products.html", context)


def Pyjama_products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.filter(type="pyjama")
    context = {"products": products, "cartItems": cartItems}
    return render(request, "pages/Pyjama_products.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "pages/cart.html", context)


def payment(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
    context = {"items": items, "order": order}
    return render(request, "pages/payment.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("Action:", action)
    print("Product:", productId)

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

    return JsonResponse("Item was added", safe=False)


from django.contrib import messages


from django.shortcuts import get_object_or_404


def user_login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        register_form = ExtendedUserCreationForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")

        if register_form.is_valid():
            user = register_form.save()

            # Check if Customer instance already exists for the user
            customer = get_object_or_404(Customer, user=user)

            if not customer:
                Customer.objects.create(user=user)

            login(request, user)
            return redirect("index")
        else:
            print(register_form.errors)

    else:
        login_form = AuthenticationForm()
        register_form = UserCreationForm()

    return render(
        request,
        "pages/login.html",
        {"login_form": login_form, "register_form": register_form},
    )


def user_logout(request):
    logout(request)
    return redirect("index")


from django.shortcuts import render, redirect


# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data["productId"]
#     action = data["action"]
#     quantity = data.get("quantity", 1)
#     print("Action :", action)
#     print("Product :", productId)

#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#     order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

#     if action == "add":
#         order_item.quantity += quantity
#     elif action == "remove":
#         order_item.quantity -= quantity

#     order_item.save()

#     if order_item.quantity <= 0:
#         order_item.delete()

#     order_items = order.orderitem_set.all()
#     cart_items = order_items.count()

#     cart_items_quantity = 0
#     for order_item in order_items:
#         cart_items_quantity += order_item.quantity

#     response = {
#         "cart_items": cart_items,
#         "cart_items_quantity": cart_items_quantity,
#     }
#     return JsonResponse(response)


# def update_profile_image(request):
#     if request.method == "POST":
#         form = ProfileImageForm(
#             request.POST, request.FILES, instance=request.user.customer
#         )
#         if form.is_valid():
#             form.save()
#             return redirect("profile")
#     else:
#         form = ProfileImageForm(instance=request.user.customer)
#     return render(request, "profile.html", {"form": form})

# blog/views.py


def photo_upload(request):
    if request.method == "POST":
        form = ProfileImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ProfileImageForm()
    return render(request, "pages/profile.html", {"form": form})


# Python program to view
# for displaying images
