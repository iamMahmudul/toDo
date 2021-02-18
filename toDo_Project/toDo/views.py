from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import toDoItem
# Create your views here.

def todoFunction(request):
    all_todo_items = toDoItem.objects.all()
    return render(request, 'todo.html', {'all_items':all_todo_items})


def addTodo(request):
    new_item = toDoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deletetodo(request,todo_id):
    itemtodelete = toDoItem.objects.get(id= todo_id)
    itemtodelete.delete()
    return HttpResponseRedirect('/')
