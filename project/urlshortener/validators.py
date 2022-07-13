from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value: str) -> str:

    url_validator = URLValidator()
    reg_val: str = value
    if "http" in reg_val:
        new_value: str = reg_val
    else:
        new_value: str = 'http://' + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL")
    return new_value
