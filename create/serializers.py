from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    description = serializers.CharField(required=True, allow_blank=True, max_length=100)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)