# views.py

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

    @action(detail=True, methods=['put'])
    def update_favorites(self, request, pk=None):
        user = self.get_object()
        favorites = request.data.get('favorites', [])  # Assuming 'favorites' is passed in request data
        user.favorites = favorites
        user.save()
        return Response({'status': 'favorites updated successfully'})
