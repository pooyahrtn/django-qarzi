from django.db import models
from users.models import User
import uuid
from polymorphic.models import PolymorphicModel


CONSOLES = [
    ('PS', 'PS4'),
    ('XB', 'XBOX'),
    ('PA', 'PS3'),
]


class BaseFeed(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=6, decimal_places=4, db_index=True)
    long = models.DecimalField(max_digits=6, decimal_places=4, db_index=True)
    game = models.CharField(max_length=100)
    console = models.CharField(max_length=2,
                               choices=CONSOLES,
                               default=CONSOLES[0][0],
                               )

    created_time = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return self.user.username + '  ' + self.game

    @property
    def type(self):
        return self.__class__.__name__

    def n_reports(self):
        return ReportFeed.objects.filter(feed=self.id).distinct('reporter').count()


class LendFeed(BaseFeed):
    need_id = models.BooleanField(default=True)
    price_per_day = models.PositiveIntegerField()


class BorrowFeed(BaseFeed):
    duration = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()


class ReportFeed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    feed = models.ForeignKey(BaseFeed, on_delete=models.CASCADE, related_name='reports')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, editable=True)