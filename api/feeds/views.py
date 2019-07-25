from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import permission_classes
from . import models
from . import serializers


class BaseFeedViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin):

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class LendFeedsViewSet(BaseFeedViewSet):
    queryset = models.LendFeed.objects.all()
    serializer_class = serializers.LendSerializer
    permission_classes = (AllowAny,)


class BorrowFeedsViewSet(BaseFeedViewSet):
    queryset = models.BorrowFeed.objects.all()
    serializer_class = serializers.BorrowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


