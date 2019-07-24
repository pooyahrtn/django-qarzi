import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_number import validators as phone_number_validators


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=14,
        validators=[phone_number_validators.RegexValidator],
        unique=True,
    )

    def __str__(self):
        return self.username

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     '''create token after User created'''
#     if created:
#         # Token.objects.create(user=instance)
#         send_message.delay('00989016166854', 'much_bede_fadat_sham')
