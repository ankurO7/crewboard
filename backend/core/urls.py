from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<str:task_id>/status/', TaskStatusUpdateView.as_view(), name='task-status-update'),
    path('tasks/<str:task_id>/updates/', TaskUpdateCreateView.as_view(), name='task-updates'),

]