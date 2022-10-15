# Cars_API
My first API with Django and  REST. 

Project setup:

1. create virtual enviroment.
    pipenv install

2. access shell
    pipenv shell

3. set python interpreter.
    pipenv --venv
    copy path
    ctrl + p 
    search Python select interpreter
    past path into "Enter interpreter paht"

4. install Django
    pipenv install django

5. install mysqlconnector or mysqlclient (they work the same)
    pipenv install mysqlclient

6. install RESTframework
    pipenv install djangorestframework

once this is pushed to github. if it's cloned down all installed packages will 
automatically be installed.



Creating Django project file.
1. django-admin

Generating project
2. django-admin startproject <project name> .
        a space and . is needed after the project name 
        so that the files can be placed in the name of 
        the project folder.

        it's good practice to use project as the end
        of your projcet name so to not confuse files. 


Linking our project to to mysqlclient

1. create a local_settings.py file in the project folder.
2. in settings.py scroll to databases. 
    cut the entire section out and past it into local.settings.py
    This new file is already marked in gitignore so whatever 
    is in that file will not be pushed. 

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "cars_database",
        "HOST": "localhost",
        "USER": "****",
        "PASSWORD": "****"

    }
}

3. at the bottom of our setting.py file 

try:
    from cars_project.local_settings import *
except ImportError:
    pass

4. cut out the security key from settings.py and past into local_settings.py. 

git commits will not have user info and secret keys. 

5. connecting the djanjo applictaion to mysql workbench
    1. +sql
    2. CREATE DATABASE <database_name> *must be name of the databse created
       in the settings files. (now found in local_settings.py)
    3. lightning bolt 
    4. refresh
    5. database shold be seen under schemas. 
    6. python manage.py migrate (defined table shold be created)




App creation:
        python manage.py startapp <app_name>


Model creation:
    class <class_name> (use app_name from above)
    
    class Car(models.Model)  (django auto_imports the models class.)
        #code first approach -> model created frist and application creates our tables. 

        example model.
class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    
    #object arrtibute with money values should always
    #carry a decimal field.  

    *** update setting.py -> INSTALLED_APPS[
        "rest_framework"
        "cars"        #app name                
    ]

     Terminal entry python manage.py makemigrations cars #we can specifically tell it
        what app to look at, but it is not necessary.

    Terminal entry python manage.py makemigrations 
    This would work as well. 
    
    the app folder should now have a initial.py file create.  

    Terminal entry python manage.py migre
    




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




Admin center setup. 
    1. python manage.py createsuperuser

    2. fill out prompts.
        user name
        password (you will not get to see the pw)
        email 

    check mysql workbench auth_user execute query
    and the admin inflow will populate

    3. python manage.py runserver
       follow link
       /admin
       log on using username and pw
       users and groups shold be available for edits.

    4. registering the model with our Django admin.py
       app folder -> admin.py -> import appmodel...ex below 

       from .models import Car
    
    5. in admin.py
       admin.site.register(Car) #the model is passed in 


Changing price to an int instead of string in django.

    1. project setting.py

    2. anywere in the settng.py file add
        REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False
}

    by default django has this set to True













