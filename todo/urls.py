from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index),
    path('add_todo/', views.add_todo, name='add'),
    path('delete_todo/<int:task_id>/', views.delete_todo, name='delete'),
    path('complete_todo/<int:task_id>/', views.complete_todo, name='complete'),
    path('edit_todo/<int:task_id>/', views.edit_todo, name='edit')
]
