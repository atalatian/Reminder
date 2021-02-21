from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('addTask/', views.addTaskView.as_view(), name='addTask'),
    path('addCategory/', views.addCategoryView.as_view(), name='addCategory'),
    path('showTasks/', views.showTasksView.as_view(), name='showTasks'),
    path('showTasks/<str:sortBy>', views.showTasksView.as_view(), name='showTasks'),
    path('downloadTasks/', views.downloadTasksView.as_view(), name='downloadTasks'),
    path('showTaskDetail/<str:title>/',
         views.showTaskDetailView.as_view(), name='showTaskDetail'),
    path('showCategories/', views.showCategoriesView.as_view(), name='showCategories'),
    path('showCategoryDetail/<str:category>',
         views.showCategoryDetailView.as_view(),
         name='showCategoryDetail'),
]
