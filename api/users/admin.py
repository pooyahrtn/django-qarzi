from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        image = obj.image
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=image.url,
                width=image.width,
                height=image.height,
            )
        )
