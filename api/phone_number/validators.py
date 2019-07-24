from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(r'^00989\d{9}$', 'Phone Number should match with 00989...')
