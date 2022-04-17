from django.db import models

# Create your models here.
from restaurant.models import Restaurant, Branch


def upload_dish_image(instance, filename):
    return f'dishes/{instance.name}/{filename}'


class MenuCategory(models.Model):
    name = models.CharField(max_length=120)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to=upload_dish_image, null=True,
                              blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    since = models.DateField(null=True, blank=True)
    up_to = models.DateField(null=True, blank=True)
    dishes = models.ManyToManyField(Dish)
    branches = models.ManyToManyField(Branch)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
