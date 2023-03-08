import string
from django.core.exceptions import ValidationError


def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")