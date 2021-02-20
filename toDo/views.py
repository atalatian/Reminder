from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .forms import TaskForm
from .forms import CategoryForm
from .models import Task
from .models import Category
from django.core import serializers
# Create your views here.


class index(View):
    def get(self, request, *args, **kwargs):
        latestTasks = []
        dueTasks = Task.objects.getDueTasks()
        ordered = Task.objects.all().order_by("pk").reverse()
        for i in range(0, len(Task.objects.all())):
            latestTasks.append(ordered[i])
            if i >= 4:
                break
        return render(request, "toDo/baseChild.html", {'dueTasks': dueTasks,
                                                       'latestTasks': latestTasks})



class addTaskView(View):
    form_class = TaskForm
    template_name = 'toDo/addTask.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, self.template_name, {'form': form})


class addCategoryView(View):
    form_class = CategoryForm
    template_name = "toDo/addCategory.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('addTask'))
        return render(request, self.template_name, {'form': form})


class showTasksView(View):
    def get(self, request, *args, **kwargs):
        if self.kwargs:
            tasks = Task.objects.all().order_by(self.kwargs["sortBy"]).reverse()
            return render(request, "toDo/showTasks.html",
                          {'tasks': tasks,
                           'sorted': True,})
        else:
            Task.objects.getDueTasks()
            tasks = Task.objects.all()
            return render(request, "toDo/showTasks.html", {'tasks': tasks})


class showTaskDetailView(View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.filter(title=self.kwargs["title"]).first()
        return render(request, "toDo/showTaskDetail.html", {'task': task})


class downloadTasksView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        try:
            mixed_query = list(tasks)
            json_str = serializers.serialize('json', mixed_query)
            response = HttpResponse(json_str, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename=export.json'
        except Exception:
            raise
        return response

class showCategoriesView(View):
    def get(self, request, *args, **kwargs):
        category_task = []
        categories = Category.objects.all()
        categoriesNoTask = Category.objects.getCategories()
        print(categories)
        print(categoriesNoTask)
        for i in range(0, len(categories)):
            category_task.append({
                "key": categories[i].category,
                "tasks": categories[i].task_set.all()
            })
        return render(request, "toDo/showCategory.html", {'category_task': category_task,
                                                          'categoriesNoTask': categoriesNoTask})

class showCategoryDetailView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(category=self.kwargs["category"]).first()
        return render(request, "toDo/showCategoryDetail.html",
                      {'tasks': categories.task_set.all(), 'category': self.kwargs["category"]})



