from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category, default="uncategorized")
    priority = models.IntegerField()
    schedule = models.DateTimeField()
    def __str__(self):
        return self.title
