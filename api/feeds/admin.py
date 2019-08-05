from django.contrib import admin
from . import models


class ReportInline(admin.TabularInline):
    model = models.ReportFeed
    extra = 0


class CheckedFilter(admin.SimpleListFilter):
    title = 'Checked'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'checked'

    def lookups(self, request, model_admin):
        return (
            (1, 'Yes'),
            (0, 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        else:
            self.used_parameters[self.parameter_name] = int(self.value())

        return queryset.filter(checked=self.value())


class AdminModel(admin.ModelAdmin):
    inlines = [
        ReportInline,
    ]
    list_display = ('user', 'game', 'console', 'checked', 'n_reports')
    list_filter = ('checked', 'created_time')


admin.site.register(models.BorrowFeed, AdminModel)
admin.site.register(models.LendFeed, AdminModel)
