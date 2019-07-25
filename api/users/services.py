from .models import User
from django.shortcuts import get_object_or_404
from phone_number import services as phone_services


def auth_with_confirm_code(phone_number: str, confirm_code: str) -> User:
    is_correct = phone_services.is_confirm_code_valid(phone_number, confirm_code)
    if is_correct:
        return get_object_or_404(User, username=phone_number)


def active_user_phone(phone_number: str):
    return phone_services.confirm_phone_number(phone_number)
