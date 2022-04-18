from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class DeliveryType(models.Model):
    type = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.type


class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    direction = models.TextField(blank=True)
    delivery_type = models.ManyToManyField(DeliveryType)

    def __str__(self):
        return f'branch (id={self.id}) - {self.restaurant.name}'
