from rest_framework import serializers
from . import models
from users.serializers import PublicUserSerializer
from utils.PolymorphicSerializer import PolymorphicSerializer
from django.shortcuts import get_object_or_404

BASE_FEED_FIELDS = (
    'user',
    'game',
    'console',
    'id',
    'type',
    'created_time',
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


class CombinedSerializer(PolymorphicSerializer):
    class Meta:
        model = models.BaseFeed

    def get_serializer_map(self):
        """
        Return serializer map
        """
        return {
            models.LendFeed.__name__: LendSerializer,
            models.BorrowFeed.__name__: BorrowSerializer,
        }

    def update(self, instance, validated_data):
        pass


class ReportSerializer(serializers.ModelSerializer):
    reporter = serializers.PrimaryKeyRelatedField(read_only=True)
    feed_id = serializers.UUIDField(required=True)

    class Meta:
        model = models.ReportFeed
        fields = ('reporter', 'feed_id')

    def create(self, validated_data):
        feed_id = validated_data.pop('feed_id')
        feed = get_object_or_404(models.BaseFeed, id=feed_id)
        instance = self.Meta.model.objects.create(**validated_data, feed=feed)
        return instance
