from django.contrib import admin
from todos.models import TodoList

# Register your models here.


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list = (
        'id',
        'name',
        'created_on'
    )
