from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:task_id>/', views.delete_todo),
    path('complete_todo/<int:task_id>/', views.complete_todo),
    path('edit_todo/<int:task_id>/', views.edit_todo)
]
