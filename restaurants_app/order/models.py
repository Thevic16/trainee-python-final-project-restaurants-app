from django.db import models

from dish.models import Dish
from person.models import Person
from restaurant.models import Branch


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Order(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    delivery_type = models.ForeignKey(Status, on_delete=models.CASCADE)
    direction = models.CharField(max_length=120)
    client = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'Order (id={self.id})'


class ItemType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ItemOrder(models.Model):
    quantity = models.IntegerField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
