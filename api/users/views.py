from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsUser
from .serializers import CreateUserSerializer, UserSerializer, TokenObtainSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUser,)

    def get_object(self):
        return self.request.user


    # def update(self, request, *args, **kwargs):
    #

class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class TokenObtainView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer
