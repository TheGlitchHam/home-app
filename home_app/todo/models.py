from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class TodoEntry(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now())
    due_date = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def check_todo(self):
        self.is_done = True
        self.save()

    class Meta:
        ordering = ['created_date']
