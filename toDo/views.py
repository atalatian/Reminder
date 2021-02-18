from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from .forms import TaskForm
from .forms import CategoryForm
from .models import Task
from django.core import serializers
# Create your views here.


class addTaskView(View):
    form_class = TaskForm
    template_name = 'addTask.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
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
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})


class showTasksView(View):
    def get(self, request, *args, **kwargs):
        if self.kwargs:
            tasks = Task.objects.all().order_by(self.kwargs["sortBy"])
            return render(request, "showTasks.html",
                          {'tasks': tasks,
                           'sorted': True,})
        else:
            tasks = Task.objects.all()
            return render(request, "showTasks.html", {'tasks': tasks})


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