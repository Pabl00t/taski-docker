"""Модуль views: содержит представления API для работы с задачами."""

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """Представление для модели Task с CRUD-операциями."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """
        Обрабатывает удаление задачи.

        Возвращает сериализованные данные удалённого объекта
        с HTTP статусом 200.
        """
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
