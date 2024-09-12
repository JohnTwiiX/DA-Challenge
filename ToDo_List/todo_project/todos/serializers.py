from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'completed', 'creator']
        read_only_fields = ['creator']