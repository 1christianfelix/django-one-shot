from django.shortcuts import redirect, render, get_object_or_404
from todos.models import TodoList

# Create your views here.


def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    print(todo_lists)
    context = {
        'todo_lists': todo_lists
    }
    return render(request, "todos/todos.html", context)
