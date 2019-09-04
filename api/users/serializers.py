from rest_framework import serializers, exceptions
from .models import User
import uuid
from phone_number import services as phone_service
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import services


class UserSerializer(serializers.ModelSerializer):
    """
    Default User Serializer
    """
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'image', 'notification_token', 'is_active')
        read_only_fields = ('username', 'id')


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Create User Serializer
    """
    username = serializers.RegexField(
        r'^00989\d{9}$',
        required=True,
        # validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        username = validated_data['username']

        found_user = User.objects.filter(username=username).first()
        if found_user:
            found_user.is_active = True
            found_user.save()
            phone_service.send_user_message(found_user)
            return found_user
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
        data['user'] = UserSerializer(self.user).data
        return data


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'image')
