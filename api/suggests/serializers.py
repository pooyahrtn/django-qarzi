from rest_framework import serializers
from . import models
from feeds.serializers import CombinedSerializer
from utils.PolymorphicSerializer import PolymorphicSerializer
from users.serializers import UserSerializer
from . import services


BASE_FIELDS = ('id', 'feed', 'type', 'feed_id')
READ_ONLY_FIELDS = ('id', 'type')
LEND_FIELDS = BASE_FIELDS + ('need_id',)
BORROW_FIELDS = BASE_FIELDS + ('duration',)


class GenericSuggestSerializer(serializers.ModelSerializer):
    feed = CombinedSerializer(read_only=True)
    from_user = UserSerializer(read_only=True)
    feed_id = serializers.UUIDField(write_only=True, required=True)
    type = serializers.CharField(read_only=True)

##############################################################


class OutcomeBorrowSuggestSerializer(GenericSuggestSerializer):

    class Meta:
        model = models.BorrowSuggest
        fields = BORROW_FIELDS
        read_only_fields = READ_ONLY_FIELDS

    def create(self, validated_data):
        return services.create_borrow_suggest(
            validated_data['from_user'],
            validated_data['feed_id'],
            validated_data['duration']
        )


class OutcomeLendSuggestSerializer(GenericSuggestSerializer):

    class Meta:
        model = models.LendSuggest
        fields = LEND_FIELDS
        read_only_fields = READ_ONLY_FIELDS

    def create(self, validated_data):
        return services.create_lend_suggest(
            validated_data['from_user'],
            validated_data['feed_id'],
            validated_data['need_id']
        )


##############################################################


class IncomeLendSuggestSerializer(GenericSuggestSerializer):
    class Meta:
        model = models.LendSuggest
        fields = LEND_FIELDS + ('from_user',)


class IncomeBorrowSuggestSerializer(GenericSuggestSerializer):
    class Meta:
        model = models.BorrowSuggest
        fields = BORROW_FIELDS + ('from_user',)


##############################################################


class CombinedIncomeSuggestSerializer(PolymorphicSerializer):

    class Meta:
        model = models.BaseSuggest

    def get_serializer_map(self):
        return {
            models.BorrowSuggest.__name__: IncomeBorrowSuggestSerializer,
            models.LendSuggest.__name__: IncomeLendSuggestSerializer,
        }

    def update(self, instance, validated_data):
        pass


class CombinedOutcomeSuggestSerializer(PolymorphicSerializer):

    class Meta:
        model = models.BaseSuggest

    def get_serializer_map(self):
        return {
            models.BorrowSuggest.__name__: OutcomeBorrowSuggestSerializer,
            models.LendSuggest.__name__: OutcomeLendSuggestSerializer,
        }

    def update(self, instance, validated_data):
        pass


##############################################################

