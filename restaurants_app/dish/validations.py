from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validator_no_negative(num: int) -> int:
    """
    Validate that the number is not negative

    Args:
        num (int): Input number

    Raises:
        ValidationError: The inserted number has to be '0' or positive

    Return:
        num (int): Input number
    """
    if num < 0:
        raise ValidationError("The inserted number has to be '0' or positive")

    return num


def validate_date1_low_date2(date1: date, date2: date, field_date1: str,
                             field_date2: str):
    """
    Validate that date1 is not lower or equal than date2

    Args:
        date1 (date): Input date1
        date2 (date): Input date2
        field_date1 (date): Name field date1
        field_date2 (date): Name field date2

    Raises:
        ValidationError: date2 has to be after the date1
    """
    if date1 > date2:
        raise ValidationError({field_date2: _('This date has to be'
                                              f' after the {field_date1}')
                               }
                              )
