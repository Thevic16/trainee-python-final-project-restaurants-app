from django.db import models


# Create your models here.
from restaurant.models import Restaurant


class MenuCategory(models.Model):
    name = models.CharField(max_length=120)


class Dish(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    delete = models.BooleanField()


class Promotion(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    since = models.DateField(null=True, blank=True)
    up_to = models.DateField(null=True, blank=True)
    dishes = models.ManyToManyField(Dish)
