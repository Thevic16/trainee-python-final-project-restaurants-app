from django.db import models


class FoodType(models.Model):
    food = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.food


class PayType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=120, unique=True)
    food_type = models.ForeignKey(
        FoodType, on_delete=models.PROTECT, null=True)
    active = models.BooleanField(default=True)
    pay_type = models.ForeignKey(PayType, on_delete=models.PROTECT, null=True)
    max_admins = models.PositiveIntegerField(default=5)
    max_branches = models.PositiveIntegerField(default=5)
    monthly_pay = models.PositiveIntegerField(default=5)
    commission = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    direction = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.direction} (Restaurant: {self.restaurant.name})'


class DeliveryType(models.Model):
    type = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.type


class PayDay(models.Model):
    day = models.PositiveIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Pay(models.Model):
    pay = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    month_payed = models.PositiveSmallIntegerField()
    pay_type = models.ForeignKey(PayType, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
