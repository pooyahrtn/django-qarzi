from rest_framework import serializers
from . import models
from users.serializers import PublicUserSerializer

BASE_FEED_FIELDS = (
    'user',
    'lat',
    'long',
    'game',
    'console',
    'id',
)

LEND_FIELDS = BASE_FEED_FIELDS + ('need_id', 'price_per_day')
BORROW_FIELDS = BASE_FEED_FIELDS + ('duration', 'price')


class LendSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)

    class Meta:
        model = models.LendFeed
        fields = LEND_FIELDS


class BorrowSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)

    class Meta:
        model = models.BorrowFeed
        fields = BORROW_FIELDS

