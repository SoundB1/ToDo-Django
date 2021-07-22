from django.contrib import admin
from .models import Task

class TaskCreatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Task, TaskCreatedAdmin)