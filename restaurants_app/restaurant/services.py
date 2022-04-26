from restaurant.models import Pay, PayType


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
