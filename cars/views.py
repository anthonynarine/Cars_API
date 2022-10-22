
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from dealerships.models import Dealership
from .serializers import CarSerializer
from .models import Car
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"]) #decerator
def cars_list(request):
    """"function that returns all Cars on the table and create a new car to add"""
    if request.method == "GET":
    #code below will run for a get request
        dealership_name = request.query_params.get("dealership")
        print(dealership_name) #used for testing 
        queryset = Car.objects.all()       
        if dealership_name:
            queryset = queryset.filter(dealership__name=dealership_name)
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(["GET", "PUT", "DELETE"])
def car_detail(request, pk): 
    """function to GET + UPDATE + DELETE a car details by a pk"""
    queryset = get_object_or_404(Car, pk=pk)  #now available for ALL REQUEST (GET,PUT,DELETE). 
    if request.method == "GET":
        serializer = CarSerializer(queryset);
        return Response(serializer.data)  
    elif request.method == "PUT":
        serializer = CarSerializer(queryset, data=request.data); #2nd arguement data is added tis take a look  
        serializer.is_valid(raise_exception=True)           # incoming JSON data and compares it to the  
        serializer.save()                                   # current version of the object and update it
        return Response(serializer.data)                    # in the database. 
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

    
    




        