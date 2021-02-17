from django.urls import path

from . import views

urlpatterns = [
    path('addTask/', views.addTaskView.as_view(), name='index'),
]
