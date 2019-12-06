from django.shortcuts import render
from django.http import HttpResponse
# Resonse
from django.http.response import JsonResponse

# Parsers
from rest_framework.parsers import JSONParser
# Viewsets
from rest_framework import viewsets, status

# Security
from django.views.decorators.csrf import csrf_exempt

# Model
from django.contrib.auth.models import User
from flights.models import Schedule

# Serializers
from flights.serializers import UserSerializer, ScheduleSerializer


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello! Example Rest App </h1>")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# APIs
# Creating APIs without a key
# /flights/
@csrf_exempt
def flight_list(request):
    # Get all
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        schedules_serializer = ScheduleSerializer(schedules, many=True)
        return JsonResponse(schedules_serializer.data, safe=False)

    # Add one
    if request.method == 'POST':
        schedule_data = JSONParser().Parsers(request)
        schedule_serializer = ScheduleSerializer(data=schedule_data)

        # Checking data is valid
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete all
    if request.method == 'DELETE':
        Schedule.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Creating APIs with a key
# /flights/id/
@csrf_exempt
def flight_detail(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

     # Retrive one
    if request.method == 'GET':
        schedule_serializer = ScheduleSerializer(schedule)
        return JsonResponse(schedule_serializer.data)

    # Updating one
    if request.method == 'PUT':
        schedule_data = JSONParser().Parsers(request)
        schedule_serializer = ScheduleSerializer(schedule, data=schedule_data)

        # Checking data is valid
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete one
    if request.method == 'DELETE':
        schedule.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

