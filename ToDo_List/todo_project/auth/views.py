from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo-list') 
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login_user')