from django.contrib import admin
from . import models

admin.site.register(models.BorrowFeed, admin.ModelAdmin)
admin.site.register(models.LendFeed, admin.ModelAdmin)