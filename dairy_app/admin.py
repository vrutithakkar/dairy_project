from django.contrib import admin
from .models import Farmer, Staff, Animal, Product, Bill

admin.site.register(Farmer)
admin.site.register(Staff)
admin.site.register(Animal)
admin.site.register(Product)
admin.site.register(Bill)
