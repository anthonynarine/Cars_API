from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status

from cars import serializers

@api_view(["GET", "POST"]) #decerator
def cars_list(request):

    if request.method == "GET":
    #code below will run for a get request
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(["GET"])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car);
        return Response(serializer.data)  
     
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    




        