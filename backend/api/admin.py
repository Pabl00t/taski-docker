"""Модуль admin: описывает административные интерфейсы Django."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Task."""

    list_display = ("title", "description", "completed")


admin.site.register(Task, TaskAdmin)
