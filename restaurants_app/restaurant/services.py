from django.shortcuts import get_object_or_404
from restaurant.models import Pay, PayType, Restaurant


class PayServices:

    @staticmethod
    def commission_pay(item, order):
        if item.promotion:
            price = item.promotion.price
        else:
            price = item.dish.price
        pay = Pay(pay=price * item.quantity,
                  pay_type=PayType.objects.get_or_create(name="commission")[0],
                  restaurant=order.branch.restaurant)
        pay.save()
        return pay

    @staticmethod
    def monthtly_pay(restaurant_id, month_payed):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        pay = restaurant.monthly_pay * restaurant.max_branches
        payment = Pay(
            pay=pay,
            pay_type=restaurant.pay_type,
            restaurant=restaurant,
            month_payed=month_payed
        )
        payment.save()
        return payment
