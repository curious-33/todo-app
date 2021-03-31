from django.urls import path
from .views import (
    APIOverview,
    TodoListView,
    CompletedTodosView,
    ActiveTodosView,
    TodoView,
    CreateTodoView,
    UpdateTodoView,
    DeleteTodoView,
    deleteAllTasksView
)


urlpatterns = [
    path('', APIOverview, name="todo-overview"),
    path('todos/', TodoListView.as_view(), name="todos"),
    path('todos&is_completed=True', CompletedTodosView.as_view(), name="completed-todos"),
    path('todos&active=True', ActiveTodosView.as_view(), name="active-todos"),
    path('todos/<int:pk>', TodoView.as_view(), name="todo"),
    path('todos/<int:id>/update/', UpdateTodoView.as_view(), name="update-todo"),
    path('todos/<int:id>/delete/', DeleteTodoView.as_view(), name="delete-todo"),
    path('todos/delete/', deleteAllTasksView, name="delete-todos"),
    path('todos/create/', CreateTodoView.as_view(), name="create-todo"),
]