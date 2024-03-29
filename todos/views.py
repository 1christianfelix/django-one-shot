from django.shortcuts import redirect, render, get_object_or_404
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm

# Create your views here.


def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    # print(todo_lists)
    context = {
        'todo_lists': todo_lists
    }
    return render(request, "todos/todos.html", context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        'todo_items': todo_list
    }
    return render(request, 'todos/todos_detail.html', context)


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm()

    context = {
        "form": form
    }

    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    # print(todo_list)
    if request.method == "POST":
        # THIS IS IMPRTnt
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail", id=todo_list.id)
    else:
        # THIS IS IMPRTnt
        form = TodoListForm(instance=todo_list)

    context = {
        'form': form
    }

    return render(request, "todos/update.html", context)


def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()

    context = {
        'form': form
    }

    return render(request, "todos/new_item.html", context)


def todo_item_update(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)

    else:
        form = TodoItemForm(instance=item)

    context = {
        'form': form
    }

    return render(request, "todos/update_item.html", context)
