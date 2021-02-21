from django.db import models
import datetime

class CategoryManager(models.Manager):
    def getCategories(self):
        result = []
        categories = Category.objects.all()
        for category in categories:
            if len(category.task_set.all()) == 0:
                result.append(category)
        return result


class Category(models.Model):
    category = models.CharField(max_length=255)
    objects = CategoryManager()
    def __str__(self):
        return self.category


class TaskManager(models.Manager):
    def getDueTasks(self):
        result = []
        tasks = Task.objects.all()
        for task in tasks:
            pack = {}
            pack["task"] = task
            currentDateTime = datetime.datetime.now().replace(tzinfo=None)
            taskDateTime = task.schedule.replace(tzinfo=None)
            delta = taskDateTime - currentDateTime
            if delta.days < 0:
                pack["due"] = True
            else:
                pack["due"] = False
            result.append(pack)
        return result


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    priority = models.IntegerField()
    schedule = models.DateTimeField()
    objects = TaskManager()

    def __str__(self):
        return self.title

