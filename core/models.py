from django.db import models

class TaskModel(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name