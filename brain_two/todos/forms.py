from django.forms import ModelForm
from todos.models import TodoList


class TodoListForm(ModelForm):
    # Meta is an Inner class
    # used to customize the form
    class Meta:
        model = TodoList
        fields = (
            "name",
        )
