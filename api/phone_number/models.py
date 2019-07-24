from django.db import models
import uuid
from users.models import User
from . import validators


class PhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(
        max_length=14,
        validators=[validators.RegexValidator],
        blank=False,
        null=False,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    last_sent_time = models.DateTimeField(auto_now_add=True)
    retries = models.PositiveSmallIntegerField(default=0)
    confirmed = models.BooleanField(default=False)
    confirm_code = models.CharField(max_length=6)

    def __str__(self):
        return self.phone_number
