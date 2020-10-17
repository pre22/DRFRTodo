from rest_framework import generics
from todos.models import Todo
from todos.serializers import TodoSerializer


# Displays all todos
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Displays a single model instance of each todo
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
