from django.db import models
from polymorphic.models import PolymorphicModel
import uuid
from django.contrib.auth import get_user_model
from feeds.models import BaseFeed


class BaseSuggest(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='out_suggests',
        blank=False,
        null=False,
    )
    to_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='in_suggests',
        blank=False,
        null=False,
    )
    feed = models.ForeignKey(BaseFeed, on_delete=models.CASCADE, blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True, editable=True)

    @property
    def type(self):
        return self.__class__.__name__

    def __str__(self):
        return '{} to {} game: {}'.format(self.from_user.username,self.to_user.username,self.feed.game)


class BorrowSuggest(BaseSuggest):
    duration = models.PositiveSmallIntegerField()


class LendSuggest(BaseSuggest):
    need_id = models.BooleanField(default=True)


