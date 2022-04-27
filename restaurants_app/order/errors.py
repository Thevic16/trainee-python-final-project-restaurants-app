from rest_framework import status
from rest_framework.validators import ValidationError


class ItemOrderError(ValidationError):
    """Base clas for ItemOrder custom errors"""
    pass


class DishAndPromotionError(ItemOrderError):
    """Raise when a dish and promotion are passed at the same time"""

    def __init__(self, detail=None, code=None):
        detail = "Only can select promotion or dish not both"
        code = status.HTTP_400_BAD_REQUEST
        super().__init__(detail, code)


class OrderError(ValidationError):
    """Base class for order validation erros"""
    pass


class Not_Ordering_Status(OrderError):
    """Raise when a order to send does not have a ordering status"""

    def __init__(self, detail=None, code=None):
        detail = "Order not in ordering status"
        code = status.HTTP_400_BAD_REQUEST
        super().__init__(detail, code)
