from .models import PhoneNumber
from .tasks import send_message
from datetime import datetime
from secrets import randbelow
from django.conf import settings


def create_random_code():
    return randbelow(10000 - 1000) + 1000


def create_user_phone(user):
    confirm_code = create_random_code()
    phone_number = PhoneNumber(
        user=user,
        phone_number=user.username,
        confirm_code=confirm_code
    )
    phone_number.save()
    return phone_number


def send_user_message(phone_number):
    phone_number.last_sent_time = datetime.now()
    phone_number.retries += 1
    if not settings.DEBUG:
        send_message.delay(phone_number.phone_number, phone_number.confirm_code)
    return phone_number


def create_and_send_code(user):
    phone_number = create_user_phone(user)
    send_user_message(phone_number)

