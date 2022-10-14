from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"]) #decerator
def cars_list(request):


    return Response("Ok this function is working")
    