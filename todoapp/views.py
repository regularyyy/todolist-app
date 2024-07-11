from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos})

def search_page(request):
    return render(request, 'todoapp/search.html')

def retrospective_page(request):
    return render(request, 'todoapp/retrospective.html')


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    tag = request.POST['tag']
    due_date = request.POST['due_date']
    todo = ToDo.objects.create(title=title, description=description, tag=tag, due_date=due_date)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

def search(request):
    tag = request.GET.get('tag')
    todos = ToDo.objects.filter(tag=tag) if tag else ToDo.objects.all()
    return render(request, 'todoapp/search.html', {'todo_list': todos})

def completed_tasks(request):
    todos = ToDo.objects.filter(is_complete=True)
    return render(request, 'todoapp/retrospective.html', {'todo_list': todos})

def incompleted_tasks(request):
    todos = ToDo.objects.filter(is_complete=False)
    return render(request, 'todoapp/retrospective.html', {'todo_list': todos})

def task_counts(request):
    total_count = ToDo.objects.count()
    completed_count = ToDo.objects.filter(is_complete=True).count()
    incompleted_count = ToDo.objects.filter(is_complete=False).count()

    context = {
        'total_count': total_count,
        'completed_count': completed_count,
        'incompleted_count': incompleted_count,
    }
    return render(request, 'todoapp/retrospective.html', context)



