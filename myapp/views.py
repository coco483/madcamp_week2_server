from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TodoItem, User
from .serializers import TodoItemSerializer, UserSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    @action(detail=True, methods=['post'])
    def set_completed(self, request, pk=None):
        todo_item = self.get_object()
        todo_item.completed = True
        todo_item.save()
        return Response({'status': 'todo item marked as completed'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer