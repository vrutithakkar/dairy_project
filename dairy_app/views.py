from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Farmer, Staff, Animal, Product, Bill
from .forms import FarmerForm, StaffForm, AnimalForm, ProductForm, BillForm


@login_required
def home(request):
    # provide simple counts for dashboard cards
    farmers_count = 0
    animals_count = 0
    products_count = 0
    try:
        farmers_count = Farmer.objects.count()
        animals_count = Animal.objects.count()
        products_count = Product.objects.count()
    except Exception:
        pass
    return render(request, "home.html", {"farmers_count": farmers_count, "animals_count": animals_count, "products_count": products_count})


def index(request):
    """Root view: if authenticated show dashboard, else show login page."""
    if request.user.is_authenticated:
        return redirect('home')
    return user_login(request)


# Farmer
@login_required
def farmer_list(request):
    data = Farmer.objects.all()
    return render(request, "farmer_list.html", {"data": data, "bg_image": "farmers.jpeg"})

@login_required
def add_farmer(request):
    form = FarmerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("farmer_list")
    return render(request, "form.html", {"form": form, "bg_image": "farmers.jpeg"})

@login_required
def delete_farmer(request, id):
    Farmer.objects.filter(id=id).delete()
    return redirect("farmer_list")


# Staff
@login_required
def staff_list(request):
    data = Staff.objects.all()
    return render(request, "staff_list.html", {"data": data, "bg_image": "staff.png"})

@login_required
def add_staff(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("staff_list")
    return render(request, "form.html", {"form": form, "bg_image": "staff.png"})


# Animal
@login_required
def animal_list(request):
    data = Animal.objects.all()
    return render(request, "animal_list.html", {"data": data, "bg_image": "Cows-in-the-field-215859100.jpg"})

@login_required
def add_animal(request):
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("animal_list")
    return render(request, "form.html", {"form": form, "bg_image": "images-cow1.jpeg"})


# Product
@login_required
def product_list(request):
    data = Product.objects.all()
    return render(request, "product_list.html", {"data": data, "bg_image": "products.jpg"})

@login_required
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "form.html", {"form": form, "bg_image": "products.jpg"})


# Bill
@login_required
def bill_list(request):
    data = Bill.objects.all()
    return render(request, "bill_list.html", {"data": data, "bg_image": "orders.jpg"})

@login_required
def add_bill(request):
    form = BillForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("bill_list")
    return render(request, "form.html", {"form": form, "bg_image": "orders.jpg"})


# Authentication views
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form, "bg_image": "login.jpg"})


def user_logout(request):
    logout(request)
    return redirect('home')
