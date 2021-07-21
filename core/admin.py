from django.contrib import admin
from .models import TaskModel
# Register your models here.

class TaskCreatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(TaskModel, TaskCreatedAdmin)