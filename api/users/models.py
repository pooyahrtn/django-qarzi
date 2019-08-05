import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_number import validators as phone_number_validators
from stdimage import StdImageField
from .tasks import process_photo_image


def image_processor(file_name, variations, storage):
    process_photo_image.delay(file_name, variations)
    return False  # prevent default rendering


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=14,
        validators=[phone_number_validators.RegexValidator],
        unique=True,
    )
    image = StdImageField(
        upload_to='profile',
        variations={
            'thumbnail': {"width": 100, "height": 100, "crop": True}
        },
        null=True,
        blank=True,
        delete_orphans=True,
        render_variations=image_processor
    )

    def __str__(self):
        return self.username

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     '''create token after User created'''
#     if created:
#         # Token.objects.create(user=instance)
#         send_message.delay('00989016166854', 'much_bede_fadat_sham')
