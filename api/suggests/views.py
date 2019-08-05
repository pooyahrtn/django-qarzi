from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import models
from . import serializers
from . import services


class IncomeSuggestsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaseSuggest.objects.all()
    serializer_class = serializers.IncomeLendSuggestSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(to_user=self.request.user)


class OutcomeSuggestsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaseSuggest.objects.all()
    serializer_class = serializers.CombinedOutcomeSuggestSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(from_user=self.request.user)


class CreateBorrowSuggestViewSet(viewsets.GenericViewSet,
                                 mixins.CreateModelMixin):
    queryset = models.BorrowSuggest.objects.all()
    serializer_class = serializers.OutcomeBorrowSuggestSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        services.create_borrow_suggest(**serializer.validated_data, from_user=self.request.user)


class CreateLendSuggestViewSet(viewsets.GenericViewSet,
                               mixins.CreateModelMixin):
    queryset = models.LendSuggest.objects.all()
    serializer_class = serializers.OutcomeLendSuggestSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        services.create_lend_suggest(**serializer.validated_data, from_user=self.request.user)
