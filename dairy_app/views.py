from django.shortcuts import render, redirect, get_object_or_404
from .models import Farmer, Staff, Animal, Product, Bill
from .forms import FarmerForm, StaffForm, AnimalForm, ProductForm, BillForm


def home(request):
    return render(request, "home.html")


# Farmer
def farmer_list(request):
    data = Farmer.objects.all()
    return render(request, "farmer_list.html", {"data": data})

def add_farmer(request):
    form = FarmerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("farmer_list")
    return render(request, "form.html", {"form": form})

def delete_farmer(request, id):
    Farmer.objects.filter(id=id).delete()
    return redirect("farmer_list")


# Staff
def staff_list(request):
    data = Staff.objects.all()
    return render(request, "staff_list.html", {"data": data})

def add_staff(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("staff_list")
    return render(request, "form.html", {"form": form})


# Animal
def animal_list(request):
    data = Animal.objects.all()
    return render(request, "animal_list.html", {"data": data})

def add_animal(request):
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("animal_list")
    return render(request, "form.html", {"form": form})


# Product
def product_list(request):
    data = Product.objects.all()
    return render(request, "product_list.html", {"data": data})

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "form.html", {"form": form})


# Bill
def bill_list(request):
    data = Bill.objects.all()
    return render(request, "bill_list.html", {"data": data})

def add_bill(request):
    form = BillForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("bill_list")
    return render(request, "form.html", {"form": form})
