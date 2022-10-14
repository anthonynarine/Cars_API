
Serializers are good for helping to convert JSON into pyhton objects
and python objects into JSON


1. import. 
    from rest_framework import serializers

2. import app. 
    from .models import Car

3. create class.
 ~the class is always named after the model followed by Serializer 

    class CarSerializer(serializers.ModelSerializer): 
        class Meta:
            model = Car
            fields = [ "id", "make", "model", "year", "price"]  






    
    