from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    forms = TodoForm()
    todos = Todo.objects.all()           #ith display cheyth kanaan aanu (create view)
    if request.method == 'POST':         # (create view)
        form = TodoForm(request.POST)    # (create view)
        if form.is_valid():              #ezhuthiyath valid aano enn check cheyyaaan  (create view)
            form.save()                  # (create view)
            return redirect('home')

    #return HttpResponse("haii")
    return render(request, 'home.html', {'form': forms, 'todos': todos})

#update click cheyyumbol option varaanum, submit adikkumbol submit aaayi home pagelek redirect aakanum "update enn function"

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update.html', {'form': form})


def delete(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id).delete()
    return redirect( 'home')