from django.forms import ModelForm
from todos.models import TodoList, TodoItem


class TodoListForm(ModelForm):
    # Meta is an Inner class
    # used to customize the form
    class Meta:
        model = TodoList
        fields = (
            "name",
        )


class TodoItemForm(ModelForm):
    # Meta is an Inner class
    # used to customize the form
    class Meta:
        model = TodoItem
        fields = (
            "task",
            "due_date",
            "is_completed",
            "list"
        )
