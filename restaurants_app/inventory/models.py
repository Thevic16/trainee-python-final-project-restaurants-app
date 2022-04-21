from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import pre_save

from dish.models import Dish
from dish.validations import validator_no_negative
from inventory.validations import (validator_no_negative_no_zero,
                                   validator_field_exist)
from restaurant.models import Branch


# Create your models here.
from utilities.logger import Logger


class Unit(models.Model):
    name = models.CharField(max_length=120, unique=True)
    abbreviation = models.CharField(max_length=60, unique=True)

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


def recipe_model_pre_save_receiver(sender, instance, *args, **kwargs):

    try:
        # Update
        pre_save_recipe = Recipe.objects.get(id=instance.id)
        if pre_save_recipe:
            Logger.info(f'Recipe (id:{pre_save_recipe.id} has been updated)')

    except ObjectDoesNotExist:
        validator_field_exist(Recipe.objects.filter(
            ingredient__id=instance.ingredient.id,
            dish__id=instance.dish.id).count(),
                                   'ingredient', 'recipe')

        Logger.info(f'Create recipe first time, will be necessary to validate')


pre_save.connect(recipe_model_pre_save_receiver, sender=Recipe)


class Inventory(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    availability = models.DecimalField(max_digits=25, decimal_places=5,
                                       validators=[
                                           validator_no_negative])
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


def inventory_model_pre_save_receiver(sender, instance, *args, **kwargs):
    try:
        # Update
        pre_save_recipe = Inventory.objects.get(id=instance.id)
        if pre_save_recipe:
            Logger.info(f'Inventory (id:{pre_save_recipe.id} has been'
                        f' updated)')

    except ObjectDoesNotExist:
        validator_field_exist(Inventory.objects.filter(
            ingredient__id=instance.ingredient.id,
            branch__id=instance.branch.id).count(),
                                   'ingredient', 'branch')

        Logger.info(f'Create inventory first time, will be necessary to'
                    f' validate')


pre_save.connect(inventory_model_pre_save_receiver, sender=Inventory)
