from django.contrib import admin
from todos.models import TodoList, TodoItem

# Register your models here.


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_on'
    )


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
        'task',
        'due_date',
        'is_completed'
    )
