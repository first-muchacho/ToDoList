from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask


urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create_form/', CreateTask.as_view(), name='create_form'),
    path('update_task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]
