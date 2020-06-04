from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from home.models import Task
import json

# Create your views here.

def index(request):
    
    return render(request, 'home.html')
    # return HttpResponse("this is index page")

def task(request):
    return render(request, 'task.html')


@csrf_exempt
def addtask(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        # payload = json.load(request.body)
        print(payload)
        try:
            add_task = Task(test_title = payload['task_title'], test_desc = payload['task_desc'], task_date = payload['date'], task_time = payload['time'], raw_date_time = payload['raw_date_time'])
            add_task.save()

            responds = json.dumps({"err":"false", "message" : "Task Add susscfully"})
        except:
            responds = json.dumps({"err":"true", "message" : "Task Not Save"})

        
    return HttpResponse(responds, content_type='text/json')

@csrf_exempt
def fetch_task(request):
    if request.method == 'GET':
        task_list = Task.objects.all()
        # print(list( task_list.values()))
        data = list( task_list.values())
    # return HttpResponse(data, content_type="application/json")
        
        # responds = json.dumps({"task": list(task_list)})
    return JsonResponse({"err" : "false" , "data": data})


@csrf_exempt
def delete_task(request):
    if request.method == 'DELETE':
        payload = json.loads(request.body)
        try:
            deleteTask = Task.objects.get(task_id = payload['task_id'])
            deleteTask.delete()
            responds = json.dumps({"err" : "false", "message" : "Task Deleted"})
        except:
            responds = json.dumps({"err" : "true", "message" : "Task not Deleted"})
        # print(payload)
    return HttpResponse(responds, content_type='text/json')

@csrf_exempt
def update_task(request):
    # params = 0
    if request.method == 'POST':
        payload = json.loads(request.body)

        tasks = Task.objects.get(task_id = payload['task_id'])
        # print(tasks.test_title) 
        # print(tasks.test_desc) 
        # print(tasks.task_time) 

        params = {"task_id": tasks.task_id, "task_title": tasks.test_title, "task_desc":tasks.test_desc, "task_time": tasks.task_time, "task_date": tasks.task_date, "raw_date_time": tasks.raw_date_time}
        responds = json.dumps(params)
        return HttpResponse(responds, content_type='text/json')

    elif request.method == 'PUT':
        payload = json.loads(request.body)
        # try: 
        # print(type(payload['task_title']))
        tasks = Task.objects.get(task_id = payload['task_id'])
        tasks.test_title = payload['task_title']
        tasks.test_desc = payload['task_desc']
        tasks.task_time = payload['task_time']
        tasks.task_date = payload['task_date']
        tasks.raw_date_time = payload['raw_date_time']

        tasks.save() 
        responds = json.dumps({"err" : "false", "message" : "Update Successs"})
        # except:
        #     responds = json.dumps({"err" : "true", "message" : "Something west wrong"})
        return HttpResponse(responds, content_type='text/json')

    return render(request, 'update.html')