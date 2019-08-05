from . import models
from users.models import User
from feeds.models import BorrowFeed, LendFeed
from django.shortcuts import get_object_or_404


def create_borrow_suggest(from_user: User, feed_id: str, duration: int, price: int) -> bool:
    feed = get_object_or_404(LendFeed, id=feed_id)
    models.BorrowSuggest.objects.create(
        from_user=from_user,
        to_user=feed.user,
        feed=feed,
        duration=duration,
        price=price
    )
    return True


def create_lend_suggest(from_user: User, feed_id: str, need_id: int, price_per_day: int) -> bool:
    feed = get_object_or_404(BorrowFeed, id=feed_id)
    models.LendSuggest.objects.create(
        from_user=from_user,
        to_user=feed.user,
        feed=feed,
        need_id=need_id,
        price_per_day=price_per_day
    )
    return True
