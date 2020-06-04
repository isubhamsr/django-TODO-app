from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/', views.task, name='task'),
    path('add/', views.addtask, name='addtask'),
    path('fetch/', views.fetch_task, name='fetchtask'),
    path('delete/', views.delete_task, name='deletetask'),
    path('update/', views.update_task, name='updatetask'),
]