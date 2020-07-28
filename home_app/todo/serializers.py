from rest_framework import serializers
from .models import Category, TodoEntry


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoEntry
        fields = ['id', 'category', 'text', 'due_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
