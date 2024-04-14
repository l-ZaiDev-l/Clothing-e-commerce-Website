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
    customer = None  # Initialisez la variable customer à None
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
    context = {"products": products, "cartItems": cartItems, "customer": customer}
    return render(request, "pages/index.html", context)




from django.shortcuts import render, redirect
from .models import Customer


def profile_view(request):
    # Récupérer l'utilisateur connecté
    user = request.user

    # Vérifier si un Customer existe déjà pour cet utilisateur
    customer, created = Customer.objects.get_or_create(user=user)

    if request.method == "POST":
        # Update profile information
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")

        customer.name = name
        customer.email = email
        customer.phone = phone
        customer.city = city
        customer.address = address

        # Enregistrer les modifications dans la base de données
        customer.save()

        # Handle profile image upload
        form = ProfileImageForm(request.POST, request.FILES, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        # Pre-fill the form with existing data
        form = ProfileImageForm(
            instance=customer,
            initial={
                "name": customer.name,
                "email": customer.email,
                "phone": customer.phone,
                "city": customer.city,
                "address": customer.address,
            },
        )

    context = {"customer": customer, "form": form}
    return render(request, "pages/Profile.html", context)




def profile_home_view(request):
    # Récupérer l'utilisateur connecté
    user = request.user

    # Vérifier si un Customer existe déjà pour cet utilisateur
    customer, created = Customer.objects.get_or_create(user=user)

    if request.method == "POST":
        # Update profile information
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")

        customer.name = name
        customer.email = email
        customer.phone = phone
        customer.city = city
        customer.address = address

        # Enregistrer les modifications dans la base de données
        customer.save()

        # Handle profile image upload
        form = ProfileImageForm(request.POST, request.FILES, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("Profile_index")
    else:
        form = ProfileImageForm(instance=customer)

    context = {"customer": customer, "form": form}
    return render(request, "pages/Profile_index.html", context)


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
            return redirect("Profile")
        else:
            print(register_form.errors)

    else:
        login_form = AuthenticationForm()
        register_form = ExtendedUserCreationForm()

    return render(
        request,
        "pages/login.html",
        {"login_form": login_form, "register_form": register_form},
    )


def user_logout(request):
    logout(request)
    return redirect("index")


from django.shortcuts import render, redirect


# blog/views.py


def photo_upload(request):
    if request.method == "POST":
        form = ProfileImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ProfileImageForm()
    return render(request, "pages/Profile.html", {"form": form})


# Python program to view
# for displaying images

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Validate form data (add your own validation logic if needed)

        # Send email
        send_mail(
            "Contact Form Submission",
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        # Render success template or redirect to a success page
        return render(request, "pages/contact.html")

    return render(request, "pages/contact.html")
