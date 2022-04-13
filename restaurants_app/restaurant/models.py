from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=120, unique=True)


class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    direction = models.TextField(blank=True)
