from django.urls import path
from . import views
from .views import task_counts

urlpatterns = [
    path('', views.index, name='index'),
    path('search_page/', views.search_page, name='search_page'),
    path('add', views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('retrospective/', views.retrospective_page, name='retrospective'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('incompleted_tasks/', views.incompleted_tasks, name='incompleted_tasks'),
    path('task_counts/', task_counts, name='task_counts'),
]