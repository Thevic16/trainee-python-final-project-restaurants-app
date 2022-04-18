from django.core.exceptions import ValidationError


def validator_no_negative_no_zero(num: int) -> int:
    """
    Validate that the number is not negative, not zero

    Args:
        num (int): Input number

    Raises:
        ValidationError: The inserted number has positive

    Return:
        num (int): Input number
    """
    if num <= 0:
        raise ValidationError("The inserted number has to be positive")

    return num
