from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.CharField(max_length=40)
    image = models.ImageField(upload_to='food/')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=30)
    soni = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    price = models.FloatField()
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.name


class Drinks(models.Model):
    name = models.CharField(max_length=30)
    qoldiq = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    price = models.FloatField()
    image = models.ImageField(upload_to='drink/')

    def __str__(self):
        return self.name


class Orders(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity_product = models.FloatField(default=0)
    drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE, null=True)
    quantity_d = models.FloatField(null=True)

    def __str__(self):
        return self.food.name


