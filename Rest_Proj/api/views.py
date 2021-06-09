from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task
# Create your views here.

# def apiOverview(request):
#     return JsonResponse("API BASE POINT", safe=False)

# Convert to Json rest framework response
@api_view(['GET']) # Only allow GET call
def apiOverview(request):

    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
   
    # return Response("API BASE POINT", safe=False)
    return Response(api_urls)


@api_view(['GET']) # If not written, may get the error -- AssertionError at /api/task-list/ .accepted_renderer not set on Response
def TaskList(request):
    
    tasks = Task.objects.all()

    serializers = TaskSerializers(tasks, many=True) # Many tells us whether to serialize one objects or more object
    print(serializers.data)

    return Response(serializers.data) # Query our database --> Serialize it ---> return to api response


@api_view(['GET']) 
def TaskDetail(request, pk):
    
    tasks = Task.objects.get(id=pk)

    serializers = TaskSerializers(tasks, many=False) 

    return Response(serializers.data) 


@api_view(['POST']) 
def TaskCreate(request):
    serializers = TaskSerializers(data=request.data) 

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data) 



@api_view(['POST']) 
def TaskUpdate(request, pk):

    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializers(instance=tasks, data=request.data) 

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data) 


@api_view(['DELETE']) 
def TaskDelete(request, pk):

    tasks = Task.objects.get(id=pk)
    
    tasks.delete()

    return Response("Item successfully deleted !") 


