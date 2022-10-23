
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from dealerships.models import Dealership
from dealerships.serializers import DealershipSerializer
from .serializers import CarSerializer
from .models import Car
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"]) #decerator
def cars_list(request):
    """"function that returns all Cars on the table and create a new car to add"""
    if request.method == "GET":
    #code below will run for a get request w/ query parameter dealership=name
        dealership_name = request.query_params.get("dealership")
        sort_param = request.query_params.get("sort")
        
        cars = Car.objects.all()  
    #query param to get all car by dealership name         
        if dealership_name:
            cars = cars.filter(dealership__name=dealership_name)
    #query param to get all cars by dealership name order by year.      
        elif sort_param:
            cars = cars.order_by(sort_param)
            
        serializer = CarSerializer(cars, many=True)
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
    
    
    
# Custom responses - passing a custom dictionary to the view function "Response" function
@api_view()
def car_and_dealerships(request):
    cars = Car.objects.all()
    dealerships = Dealership.objects.all()
    
    car_serializer = CarSerializer(cars, many=True)
    dealerships_serializer = DealershipSerializer(dealerships,many=True)
    
    custom_response_dict = {
        "cars": car_serializer.data,
        "dealerships": dealerships_serializer.data
    }
    
    return Response(custom_response_dict)
    





    
    




        