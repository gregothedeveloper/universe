from django.contrib import admin
from .models import Task


class TaskModel(admin.ModelAdmin):
    list_display = ['title', 'description','status', 'created_at', 'due_date']
    search_fields = ['title',  'status']

# Register your models here.
admin.site.register(Task, TaskModel)