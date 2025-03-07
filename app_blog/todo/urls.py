# todo/urls.py

from django.urls import path
from .views import task_list, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, TaskDeleteMultiple
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', task_list, name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="taskdetail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="tasks-delete"),
    path('tasks/delete-multiple/', TaskDeleteMultiple.as_view(), name='delete_multiple_tasks'),
]
