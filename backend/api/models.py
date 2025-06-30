"""Модуль models: содержит описание моделей базы данных приложения API."""

from django.db import models


class Task(models.Model):
    """Модель задачи с полями заголовка, описания и статуса выполнения."""

    title = models.CharField(verbose_name="Заголовок", max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        """Возвращает строковое представление задачи (её заголовок)."""
        return self.title
