from django.urls import path
from . import views

urlpatterns = [
    path('addtask', views.addtask, name="addtask"),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),
    #undone task
    path('unmark/<int:pk>/', views.unmark, name="unmark"),
    #edit task url
    path('edit_task/<int:pk>/', views.edit_task, name="edit_task")
]