from rest_framework.pagination import CursorPagination


class CreatedTimeCursorPagination(CursorPagination):
    ordering = '-created_time'
