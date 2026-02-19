from django.db import models

# Farmer
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


# Staff
class Staff(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default='')
    role = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.name


# Animal
class Animal(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    animal_type = models.CharField(max_length=50)
    age = models.IntegerField()
    milk_per_day = models.FloatField()

    def __str__(self):
        return self.animal_type


# Dairy Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


# Bill
class Bill(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.FloatField()

    def __str__(self):
        return f"Bill {self.id}"
