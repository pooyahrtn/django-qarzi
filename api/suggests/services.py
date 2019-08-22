from . import models
from users.models import User
from feeds.models import BorrowFeed, LendFeed
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


def is_request_exists(from_user: User, feed):
    return len(models.BaseSuggest.objects.filter(from_user=from_user, feed=feed)) > 0


def is_request_valid(from_user: User, feed):
    if from_user == feed.user:
        raise ValidationError("Can not request your self")
    if is_request_exists(from_user, feed):
        raise ValidationError("Request already exists")


def create_borrow_suggest(from_user: User, feed_id: str, duration: int) -> bool:
    feed = get_object_or_404(LendFeed, id=feed_id)
    is_request_valid(from_user, feed)

    return models.BorrowSuggest.objects.create(
        from_user=from_user,
        to_user=feed.user,
        feed=feed,
        duration=duration,
    )


def create_lend_suggest(from_user: User, feed_id: str, need_id: int) -> bool:
    feed = get_object_or_404(BorrowFeed, id=feed_id)
    is_request_valid(from_user, feed)

    return models.LendSuggest.objects.create(
        from_user=from_user,
        to_user=feed.user,
        feed=feed,
        need_id=need_id,
    )