from restaurant import errors


class RestaurantValidator:
    """Validations for restaurant business logic"""

    @staticmethod
    def commission_monthly_method(commission: int, pay_type: str):
        """
        Validate if the commission is given when a commission pay method is
        selected
        """

        if pay_type == 'commission' and not commission:
            raise errors.NotCommissionGivenError()

    @staticmethod
    def commission_bte_0_100(commission: int):
        """Validate if commission is in range 0 and 100"""
        if commission:
            if not 0 < commission < 100:
                raise errors.NotCommissionBte0And100()


class PayDayValidator:
    """Validations for payday business logic"""

    @staticmethod
    def pay_day_lt_15(day: int):
        if day > 15:
            raise errors.PayDayLte15()

    @staticmethod
    def monthly_restaurant(restaurant_type: str):
        if restaurant_type != 'monthly':
            raise errors.RestaurantMustBeMonthly()


class PayValidator:
    """Validations for pay operation"""
    def valid_month(month: int):
        if month > 12:
            raise errors.MonthLte12
