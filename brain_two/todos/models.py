from django.db import models

# Create your models here.


class TodoList(models.Model):
    # this is a class, remember what classes look like!
    name = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
