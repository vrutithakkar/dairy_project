from django import forms
from .models import Farmer, Staff, Animal, Product, Bill

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
