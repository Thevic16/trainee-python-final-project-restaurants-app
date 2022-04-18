from django.db import models

from dish.models import Dish
from dish.validations import validator_no_negative
from inventory.validations import validator_no_negative_no_zero
from restaurant.models import Branch


# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - unit ({self.unit.name})'


class Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=25, decimal_places=5,
                                   validators=[validator_no_negative_no_zero])
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dish.name}'


class Inventory(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    availability = models.DecimalField(max_digits=25, decimal_places=5,
                                       validators=[
                                           validator_no_negative])
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
