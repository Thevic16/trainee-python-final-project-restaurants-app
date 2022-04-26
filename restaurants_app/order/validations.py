from order import errors


class ItemOrderValidator:

    @staticmethod
    def dish_or_promotion(dish, promotion):
        if dish and promotion:
            raise errors.DishAndPromotionError()


class OrderValidator:

    @staticmethod
    def order_preparing(order):
        if order.status.name != "ordering":
            raise errors.Not_Ordering_Status()
