from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):
    ...


admin.site.register(Log, LogAdmin)

