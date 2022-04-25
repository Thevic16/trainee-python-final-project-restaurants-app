from django.db import models

from dish.models import Dish, Promotion
from person.models import Person
from restaurant.models import Branch, DeliveryType


class Status(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


def get_sentinel_status():
    """
    function that set a order to ordering status, the order mainting the status
    while the client is choosing dishes
    """
    return Status.objects.get_or_create(name="ordering")[0]


def get_sentinel_status_id():
    return get_sentinel_status().id


class Order(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, default=get_sentinel_status_id)
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE)
    direction = models.CharField(max_length=120, null=True)
    client = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order (id={self.id})'


class ItemType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ItemOrder(models.Model):
    quantity = models.IntegerField(default=1)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Item {self.id} from order {self.order.id}"
