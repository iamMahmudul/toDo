from django.contrib import admin
from django.urls import path
from toDo.views import todoFunction, addTodo, deletetodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoFunction),
    path('addtodo/', addTodo),
    path('deletetodo/<int:todo_id>/', deletetodo),
]
