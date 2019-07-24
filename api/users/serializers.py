from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
import uuid
from phone_number import services as phone_service

class UserSerializer(serializers.ModelSerializer):
    """
    Default User Serializer
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username',)


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Create User Serializer
    """
    username = serializers.RegexField(
        r'^00989\d{9}$',
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(
            password=uuid.uuid4(),
            **validated_data
        )
        phone_service.create_and_send_code(user)
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )
