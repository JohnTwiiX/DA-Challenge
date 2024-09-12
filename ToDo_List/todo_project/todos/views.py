from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ToDo
from .forms import ToDoForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ToDoSerializer

@login_required
def todo_list(request):
    todos = ToDo.objects.filter(creator=request.user)

    if request.method == 'POST':
        if 'create' in request.POST:
            form = ToDoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.creator = request.user
                todo.save()
                return redirect('todo-list')
        elif 'update' in request.POST:
            todo_id = request.POST.get('todo_id')
            todo = get_object_or_404(ToDo, id=todo_id, creator=request.user)
            todo.completed = not todo.completed
            todo.save()
            return redirect('todo-list')
        elif 'delete' in request.POST:
            todo_id = request.POST.get('todo_id')
            todo = get_object_or_404(ToDo, id=todo_id, creator=request.user)
            todo.delete()
            return redirect('todo-list')

    form = ToDoForm()
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todos/list.html', context)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def todo_api(request, pk=None):
    if request.method == 'GET':
        if pk:
            todo = get_object_or_404(ToDo, pk=pk, creator=request.user)
            serializer = ToDoSerializer(todo)
        else:
            todos = ToDo.objects.filter(creator=request.user)
            serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        todo = get_object_or_404(ToDo, pk=pk, creator=request.user)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo = get_object_or_404(ToDo, pk=pk, creator=request.user)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
