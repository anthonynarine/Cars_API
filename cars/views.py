from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer

@api_view(["GET"]) #decerator
def cars_list(request):

    cars = Car.objects.all()

    serializer = CarSerializer(cars, many=True)

    return Response(serializer.data)
    