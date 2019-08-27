from . import models
from users.models import User
from feeds.models import BorrowFeed, LendFeed, BaseFeed
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from . import tasks


def send_suggest_notification(to_user: User, feed: BaseFeed):
    if to_user.notification_token:
        tasks.send_notification(
            to_user_token=to_user.notification_token,
            title='درخواست جدید!',
            body='شما یک درخواست جدید برای بازی {} دارید'.format(feed.game),
        )


def is_request_exists(from_user: User, feed):
    return len(models.BaseSuggest.objects.filter(from_user=from_user, feed=feed)) > 0


def is_request_valid(from_user: User, feed):
    if from_user == feed.user:
        raise ValidationError("Can not request your self")
    if is_request_exists(from_user, feed):
        raise ValidationError("Request already exists")


def create_borrow_suggest(from_user: User, feed_id: str, duration: int) -> bool:
    feed: LendFeed = get_object_or_404(LendFeed, id=feed_id)
    is_request_valid(from_user, feed)

    suggest = models.BorrowSuggest.objects.create(
        from_user=from_user,
        to_user=feed.user,
        feed=feed,
        duration=duration,
    )
    send_suggest_notification(feed.user, feed)
    return suggest


def create_lend_suggest(from_user: User, feed_id: str, need_id: int) -> bool:
    feed: BorrowFeed = get_object_or_404(BorrowFeed, id=feed_id)
    is_request_valid(from_user, feed)

    suggest = models.LendSuggest.objects.create(
        from_user=from_user,
        to_user=feed.user,
        feed=feed,
        need_id=need_id,
    )
    send_suggest_notification(feed.user, feed)
    return suggest