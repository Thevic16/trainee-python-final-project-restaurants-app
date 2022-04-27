from rest_framework.serializers import ValidationError


class RestaurantValidationError(ValidationError):
    """Base class for restaurant validation errors"""
    pass


class NotCommissionGivenError(RestaurantValidationError):
    """Raised when it's given a monthly pay method but not a commission"""

    def __init__(self, detail=None, code=None):
        detail = {
            "commission": ("The commission is mandatory when a monthly pay "
                           "method is selected")
        }
        code = 'not_commission_given'
        super().__init__(detail, code)


class NotCommissionBte0And100(RestaurantValidationError):
    """Raised when a commission is not between 0 and 100"""

    def __init__(self, detail=None, code=None):
        detail = {
            "commission": "Commissino must be between 0 and 100"
        }
        code = 'commission_not_between_0_100'
        super().__init__(detail, code)


class PayDayValidationError(ValidationError):
    """Base class for payday validation errors"""
    pass


class PayDayLte15(PayDayValidationError):
    """Raised when a day of pay is grather than 15 days"""

    def __init__(self, detail=None, code=None):
        detail = {
            "day": "The pay day choose must be less than 15 days"
        }
        code = 'day_lte_15'
        super().__init__(detail, code)


class RestaurantMustBeMonthly(PayDayValidationError):
    """Raised when a restaurant is not a monthly pay method"""

    def __init__(self, detail=None, code=None):
        detail = {
            "restaurant": "The restaurant pay type must be monthly"
        }
        code = 'restaurant_monthly'
        super().__init__(detail, code)


class PayValidationError(ValidationError):
    """Base class for pay validation errors"""
    pass


class MonthLte12(PayDayValidationError):
    """Raised when a pay choose is gt 12"""

    def __init__(self, detail=None, code=None):
        detail = {
            "month_payed": "The month must not be greather than 12"
        }
        code = 'month_payed_lt_12'
        super().__init__(detail, code)
