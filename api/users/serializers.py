from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from .models import User
import uuid
from phone_number import services as phone_service
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import services


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


class TokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = {}
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = services.auth_with_confirm_code(
            authenticate_kwargs[self.username_field],
            authenticate_kwargs['password']
        )

        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )
        services.active_user_phone(authenticate_kwargs[self.username_field])

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',)
