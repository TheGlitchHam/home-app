from rest_framework import serializers
from .models import Category, TodoEntry


class TodoSerializer(serializers.ModelSerializer):
    # without highlighter

    class Meta:
        model = TodoEntry
        fields = ['id', 'category', 'text', 'due_date']


'''


class TodoSerializer(serializers.HyperlinkedModelSerializer):

    highlight = serializers.HyperlinkedIdentityField(
        view_name='todo-highlight', format='html')

    class Meta:
        model = TodoEntry
        fields = ['id', 'category', 'highlight', 'text', 'due_date']
'''


class CategorySerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TodoEntry.objects.all())

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'todos']
