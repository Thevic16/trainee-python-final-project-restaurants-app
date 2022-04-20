from django.db import models

from restaurant.models import Restaurant


class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    direction = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.direction
