"""Модуль serializers: содержит сериализаторы для моделей API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Task."""

    class Meta:
        """Метаданные для сериализатора TaskSerializer."""

        model = Task
        fields = ("id", "title", "description", "completed")
