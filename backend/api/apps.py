"""Модуль apps: базовый конфиг для инициализации приложения в Django."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфигурация приложения API."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
