https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html

# BU PROJEDE KAYNAK KODUNDA YAPILAN DEGISIKLIKLER 'DEGISIKLIK' ADI ILE BELIRTILMISTIR. 


sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update
sudo apt-get install python3.6

wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py

sudo pip3.6 install virtualenv

mkdir myproject
cd myproject

virtualenv venv -p python3.6

source venv/bin/activate

sudo pip3.6 install django

django-admin startproject myproject

myproject/                  <-- higher level folder
 |-- myproject/             <-- django project folder
 |    |-- myproject/
 |    |    |-- __init__.py
 |    |    |-- settings.py
 |    |    |-- urls.py
 |    |    |-- wsgi.py
 |    +-- manage.py
 +-- venv/                  <-- virtual environment folder


 Our initial project structure is composed of five files:

manage.py: a shortcut to use the django-admin command-line utility. It’s used to run management commands related to our project. We will use it to run the development server, run tests, create migrations and much more.
__init__.py: this empty file tells Python that this folder is a Python package.
settings.py: this file contains all the project’s configuration. We will refer to this file all the time!
urls.py: this file is responsible for mapping the routes and paths in our project. For example, if you want to show something in the URL /about/, you have to map it here first.
wsgi.py: this file is a simple gateway interface used for deployment. You don’t have to bother about it. Just let it be for now.


 python manage.py runserver


 ####

 django-admin startapp boards

 myproject/
 |-- myproject/
 |    |-- boards/                <-- our new django app!
 |    |    |-- migrations/
 |    |    |    +-- __init__.py
 |    |    |-- __init__.py
 |    |    |-- admin.py
 |    |    |-- apps.py
 |    |    |-- models.py
 |    |    |-- tests.py
 |    |    +-- views.py
 |    |-- myproject/
 |    |    |-- __init__.py
 |    |    |-- settings.py
 |    |    |-- urls.py
 |    |    |-- wsgi.py
 |    +-- manage.py
 +-- venv/


 So, let’s first explore what each file does:

migrations/: here Django store some files to keep track of the changes you create in the models.py file, so to keep the database and the models.py synchronized.
admin.py: this is a configuration file for a built-in Django app called Django Admin.
apps.py: this is a configuration file of the app itself.
models.py: here is where we define the entities of our Web application. The models are translated automatically by Django into database tables.
tests.py: this file is used to write unit tests for the app.
views.py: this is the file where we handle the request/response cycle of our Web application.
Now that we created our first app, let’s configure our project to use it.

To do that, open the settings.py and try to find the INSTALLED_APPS variable:


# in settings.py add 'boards' to installed apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'boards',
]

Using the analogy of the square and circles from the previous comic, the yellow circle would be our boards app, and the django.contrib.admin, django.contrib.auth, etc, would be the red circles.

####

Hello, World!

Let’s write our first view. We will explore it in great detail in the next tutorial. But for now, let’s just experiment how it looks like to create a new page with Django.

Open the views.py file inside the boards app, and add the following code:

views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')


Views are Python functions that receive an HttpRequest object and returns an HttpResponse object. Receive a request as a parameter and returns a response as a result. That’s the flow you have to keep in mind!