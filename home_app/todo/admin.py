from django.contrib import admin
from todo.models import Category, TodoEntry

# Register your models here.
admin.site.register(Category)
admin.site.register(TodoEntry)
