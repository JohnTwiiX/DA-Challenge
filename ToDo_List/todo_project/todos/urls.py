from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('api/todos/', views.todo_api, name='todo-api'),
    path('api/todos/<int:pk>/', views.todo_api), 
]
