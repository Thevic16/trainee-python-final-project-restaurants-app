from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

from dish.validations import validator_no_negative, validate_date1_low_date2
from restaurant.models import Restaurant, Branch


def upload_dish_image(instance, file_name):
    return f'dishes/{instance.name}/{file_name}'


class MenuCategory(models.Model):
    name = models.CharField(max_length=120)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                validators=[validator_no_negative])
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to=upload_dish_image)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                validators=[validator_no_negative])
    since_date = models.DateField(null=True, blank=True)
    up_to = models.DateField(null=True, blank=True)
    dishes = models.ManyToManyField(Dish)
    branches = models.ManyToManyField(Branch)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def promotion_model_pre_save_receiver(sender, instance, *args, **kwargs):
    validate_date1_low_date2(instance.since_date, instance.up_to,
                             'since_date', 'up_to')


pre_save.connect(promotion_model_pre_save_receiver, sender=Promotion)
