from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from utils.CursorPagination import CreatedTimeCursorPagination


class BaseFeedViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin):

    pagination_class = CreatedTimeCursorPagination

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class LendFeedsViewSet(BaseFeedViewSet):
    queryset = models.LendFeed.objects.all()
    serializer_class = serializers.LendSerializer
    permission_classes = (AllowAny,)

    def filter_queryset(self, queryset):
        return queryset.filter(checked=True)


class BorrowFeedsViewSet(BaseFeedViewSet):
    queryset = models.BorrowFeed.objects.all()
    serializer_class = serializers.BorrowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def filter_queryset(self, queryset):
        return queryset.filter(checked=True)


class MyFeedsViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin
                     ):
    queryset = models.BaseFeed.objects.all()
    serializer_class = serializers.CombinedSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CreatedTimeCursorPagination

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)


class ReportViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin):
    queryset = models.ReportFeed.objects.all()
    serializer_class = serializers.ReportSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # data = serializer.validated_data
        # feed = get_object_or_404(models.BaseFeed, id=data['feed_id'])
        # models.ReportFeed.objects.create(
        #     reporter=self.request.user,
        #     feed=feed,
        # )
        serializer.save(reporter=self.request.user)
