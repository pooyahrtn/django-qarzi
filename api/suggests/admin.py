from django.contrib import admin
from . import models

admin.site.register(models.LendSuggest, admin.ModelAdmin)
admin.site.register(models.BorrowSuggest, admin.ModelAdmin)
