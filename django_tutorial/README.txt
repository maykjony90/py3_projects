Her seyden once url dosyasina ilgili URL'i ekle.




https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html

# BU PROJEDE KAYNAK KODUNDA YAPILAN DEGISIKLIKLER 'DEGISIKLIK' ADI ILE BELIRTILMISTIR.
# KAC LINE'DA DEGISIKLIK YAPILDIGI ISE '2 ln' (two lines) OLARAK BELIRTILMISTIR. 


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

# IMPORTANT NOTE!!!!
Just mentioning that Python 3.6 comes with the "venv" package in the stdlib. So you don't need to install virtualenv unless I missed something. Just replace "virtualenv venv -p python3" with "python3 -m venv venv"

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

Now we have to tell Django when to serve this view. It’s done inside the urls.py file:

urls.py

	from django.conf.urls import url
	from django.contrib import admin

	from boards import views

	urlpatterns = [
	    url(r'^$', views.home, name='home'),
	    url(r'^admin/', admin.site.urls),
	]


If you compare the snippet above with your urls.py file, you will notice I added the following new line: url(r'^$', views.home, name='home') and imported the views module from our app boards using from boards import views.

As I mentioned before, we will explore those concepts in great detail later on.

But for now, Django works with regex to match the requested URL. For our home view, I’m using the ^$ regex, which will match an empty path, which is the homepage (this url: http://127.0.0.1:8000). If I wanted to match the URL http://127.0.0.1:8000/homepage/, my url would be: url(r'^homepage/$', views.home, name='home').



models.py

	from django.db import models
	from django.contrib.auth.models import User


	class Board(models.Model):
	    name = models.CharField(max_length=30, unique=True)
	    description = models.CharField(max_length=100)


	class Topic(models.Model):
	    subject = models.CharField(max_length=255)
	    last_updated = models.DateTimeField(auto_now_add=True)
	    board = models.ForeignKey(Board, related_name='topics')
	    starter = models.ForeignKey(User, related_name='topics')


	class Post(models.Model):
	    message = models.TextField(max_length=4000)
	    topic = models.ForeignKey(Topic, related_name='posts')
	    created_at = models.DateTimeField(auto_now_add=True)
	    updated_at = models.DateTimeField(null=True)
	    created_by = models.ForeignKey(User, related_name='posts')
	    updated_by = models.ForeignKey(User, null=True, related_name='+')




SUBLIME TEXT 3 
! + TAB 	= html structure


Open the Terminal , activate the virtual environment, go to the folder where the manage.py file is, and run the commands below:

python manage.py makemigrations

As an output you will get something like this:

Migrations for 'boards':
  boards/migrations/0001_initial.py
    - Create model Board
    - Create model Post
    - Create model Topic
    - Add field topic to post
    - Add field updated_by to post



The migration files are translated into SQL statements. If you are familiar with SQL, you can run the following command to inspect the SQL instructions that will be executed in the database:

	python manage.py sqlmigrate boards 0001



The next step now is to apply the migration we generated to the database:

python manage.py migrate



You can start a Python shell with our project loaded using the manage.py utility:

python manage.py shell
Python 3.6.2 (default, Jul 17 2017, 23:14:31)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>



Let’s start by importing the Board class:

from boards.models import Board
To create a new board object, we can do the following:

board = Board(name='Django', description='This is a board about Django.')
To persist this object in the database, we have to call the save method:

board.save()
The save method is used both to create and update objects. Here Django created a new object because the Board instance had no id. After saving it for the first time, Django will set the id automatically:

board.id
1
You can access the rest of the fields as Python attributes:

board.name
'Django'
board.description
'This is a board about Django.'
To update a value we could do:

board.description = 'Django discussion board.'
board.save()
Every Django model comes with a special attribute; we call it a Model Manager. You can access it via the Python attribute objects. It is used mainly to execute queries in the database. For example, we could use it to directly create a new Board object:

board = Board.objects.create(name='Python', description='General discussion about Python.')
board.id
2
board.name
'Python'
So, right now we have two boards. We can use the objects to list all existing boards in the database:

Board.objects.all()
<QuerySet [<Board: Board object>, <Board: Board object>]>
The result was a QuerySet. We will learn more about that later on. Basically, it’s a list of objects from the database. We can see that we have two objects, but we can only read Board object. That’s because we haven’t defined the __str__ method in the Board model.

The __str__ method is a String representation of an object. We can use the board name to represent it.

First, exit the interactive console:

exit()
Now edit the models.py file inside the boards app:

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
Let’s try the query again. Open the interactive console again:

python manage.py shell
from boards.models import Board

Board.objects.all()
<QuerySet [<Board: Django>, <Board: Python>]>
Much better, right?

We can treat this QuerySet like a list. Let’s say we wanted to iterate over it and print the description of each board:

boards_list = Board.objects.all()
for board in boards_list:
    print(board.description)
The result would be:

Django discussion board.
General discussion about Python.
Similarly, we can use the model Manager to query the database and return a single object. For that we use the get method:

django_board = Board.objects.get(id=1)

django_board.name
'Django'
But we have to be careful with this kind of operation. If we try to get an object that doesn’t exist, for example, a board with id=3, it will raise an exception:

board = Board.objects.get(id=3)

boards.models.DoesNotExist: Board matching query does not exist.
We can use the get method with any model field, but preferably use a field that can uniquely identify an object. Otherwise, the query may return more than one object, which will cause an exception.

Board.objects.get(name='Django')
<Board: Django>
Note that the query is case sensitive, a lower case “django” would not match:

Board.objects.get(name='django')
boards.models.DoesNotExist: Board matching query does not exist.




Operation	Code sample
Create an object without saving	board = Board()
Save an object (create or update)	board.save()
Create and save an object in the database	Board.objects.create(name='...', description='...')
List all objects	Board.objects.all()
Get a single object, identified by a field	Board.objects.get(id=1)



boards/views.py

from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)




    templates/home.html

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
  </head>
  <body>
    <h1>Boards</h1>

    {% for board in boards %}
      {{ board.name }} <br>
    {% endfor %}

  </body>
</html>




Open the settings.py inside the myproject directory and search for the TEMPLATES variable and set the DIRS key to os.path.join(BASE_DIR, 'templates'):




We can debug this using the Python shell:

python manage.py shell
from django.conf import settings

settings.BASE_DIR
'/Users/vitorfs/Development/myproject'

import os

os.path.join(settings.BASE_DIR, 'templates')
'/Users/vitorfs/Development/myproject/templates'



boards/views.py

from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


We can improve the HTML template to use a table instead:

templates/home.html

	<!DOCTYPE html>
	<html>
	  <head>
	    <meta charset="utf-8">
	    <title>Boards</title>
	  </head>
	  <body>
	    <h1>Boards</h1>

	    <table border="1">
	      <thead>
	        <tr>
	          <th>Board</th>
	          <th>Posts</th>
	          <th>Topics</th>
	          <th>Last Post</th>
	        </tr>
	      </thead>
	      <tbody>
	        {% for board in boards %}
	          <tr>
	            <td>
	              {{ board.name }}<br>
	              <small style="color: #888">{{ board.description }}</small>
	            </td>
	            <td>0</td>
	            <td>0</td>
	            <td></td>
	          </tr>
	        {% endfor %}
	      </tbody>
	    </table>
	  </body>
	</html>


Now we can test if Django returned the correct view function for the requested URL. This is also a useful test because as we progress with the development, you will see that the urls.py module can get very big and complex. The URL conf is all about resolving regex. There are some cases where we have a very permissive URL, so Django can end up returning the wrong view function.

Here’s how we do it:

boards/tests.py

from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
In the second test, we are making use of the resolve function. Django uses it to match a requested URL with a list of URLs listed in the urls.py module. This test will make sure the URL /, which is the root URL, is returning the home view.

Test it again:

python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.027s

OK
Destroying test database for alias 'default'...
To see more detail about the test execution, set the verbosity to a higher level:

python manage.py test --verbosity=2
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, boards, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying boards.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_home_url_resolves_home_view (boards.tests.HomeTests) ... ok
test_home_view_status_code (boards.tests.HomeTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.017s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Verbosity determines the amount of notification and debug information that will be printed to the console; 0 is no output, 1 is normal output, and 2 is verbose output.



URL

We will start by editing the urls.py inside the myproject folder:

myproject/urls.py

from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^admin/', admin.site.urls),
]
This time let’s take a moment and analyze the urlpatterns and url.

The URL dispatcher and URLconf (URL configuration) are fundamental parts of a Django application. In the beginning, it can look confusing; I remember having a hard time when I first started developing with Django.

In fact, right now the Django Developers are working on a proposal to make simplified routing syntax. But for now, as per the version 1.11, that’s what we have. So let’s try to understand how it works.

A project can have many urls.py distributed among the apps. But Django needs a url.py to use as a starting point. This special urls.py is called root URLconf. It’s defined in the settings.py file.

myproject/settings.py

ROOT_URLCONF = 'myproject.urls'
It already comes configured, so you don’t need to change anything here.

When Django receives a request, it starts searching for a match in the project’s URLconf. It starts with the first entry of the urlpatterns variable, and test the requested URL against each url entry.

If Django finds a match, it will pass the request to the view function, which is the second parameter of the url. The order in the urlpatterns matters, because Django will stop searching as soon as it finds a match. Now, if Django doesn’t find a match in the URLconf, it will raise a 404 exception, which is the error code for Page Not Found.

This is the anatomy of the url function:

def url(regex, view, kwargs=None, name=None):
    # ...
regex: A regular expression for matching URL patterns in strings. Note that these regular expressions do not search GET or POST parameters. In a request to http://127.0.0.1:8000/boards/?page=2 only /boards/ will be processed.
view: A view function used to process the user request for a matched URL. It also accepts the return of the django.conf.urls.include function, which is used to reference an external urls.py file. You can, for example, use it to define a set of app specific URLs, and include it in the root URLconf using a prefix. We will explore more on this concept later on.
kwargs: Arbitrary keyword arguments that’s passed to the target view. It is normally used to do some simple customization on reusable views. We don’t use it very often.
name: A unique identifier for a given URL. This is a very important feature. Always remember to name your URLs. With this, you can change a specific URL in the whole project by just changing the regex. So it’s important to never hard code URLs in the views or templates, and always refer to the URLs by its name.



Basic URLs

Basic URLs are very simple to create. It’s just a matter of matching strings. For example, let’s say we wanted to create an “about” page, it could be defined like this:

from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
]
We can also create deeper URL structures:

from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^about/company/$', views.about_company, name='about_company'),
    url(r'^about/author/$', views.about_author, name='about_author'),
    url(r'^about/author/vitor/$', views.about_vitor, name='about_vitor'),
    url(r'^about/author/erica/$', views.about_erica, name='about_erica'),
    url(r'^privacy/$', views.privacy_policy, name='privacy_policy'),
]
Those are some examples of simple URL routing. For all the examples above, the view function will follow this structure:

def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})
Advanced URLs

A more advanced usage of URL routing is achieved by taking advantage of the regex to match certain types of data and create dynamic URLs.

For example, to create a profile page, like many services do like github.com/vitorfs or twitter.com/vitorfs, where “vitorfs” is my username, we can do the following:

from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
]
This will match all valid usernames for a Django User model.

Now observe that the example above is a very permissive URL. That means it will match lots of URL patterns because it is defined in the root of the URL, with no prefix like /profile/<username>/. In this case, if we wanted to define a URL named /about/, we would have do define it before the username URL pattern:

from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
]
If the “about” page was defined after the username URL pattern, Django would never find it, because the word “about” would match the username regex, and the view user_profile would be processed instead of the about view function.

There are some side effects to that. For example, from now on, we would have to treat “about” as a forbidden username, because if a user picked “about” as their username, this person would never see their profile page.



 Sidenote: If you want to design cool URLs for user profiles, the easiest solution to avoid URL collision is by adding a prefix like /u/vitorfs/, or like Medium does /@vitorfs/, where "@" is the prefix.

If you want no prefix at all, consider using a list of forbidden names like this: github.com/shouldbee/reserved-usernames. Or another example is an application I developed when I was learning Django; I created my list at the time: github.com/vitorfs/parsifal/.

Those collisions are very common. Take GitHub for example; they have this URL to list all the repositories you are currently watching: github.com/watching. Someone registered a username on GitHub with the name "watching," so this person can't see his profile page. We can see a user with this username exists by trying this URL: github.com/watching/repositories which was supposed to list the user's repositories, like mine for example github.com/vitorfs/repositories.
The whole idea of this kind of URL routing is to create dynamic pages where part of the URL will be used as an identifier for a certain resource, that will be used to compose a page. This identifier can be an integer ID or a string for example.

Initially, we will be working with the Board ID to create a dynamic page for the Topics. Let’s read again the example I gave at the beginning of the URLs section:

url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics')
The regex \d+ will match an integer of arbitrary size. This integer will be used to retrieve the Board from the database. Now observe that we wrote the regex as (?P<pk>\d+), this is telling Django to capture the value into a keyword argument named pk.

Here is how we write a view function for it:

def board_topics(request, pk):
    # do something...
Because we used the (?P<pk>\d+) regex, the keyword argument in the board_topics must be named pk.

If we wanted to use any name, we could do it like this:

url(r'^boards/(\d+)/$', views.board_topics, name='board_topics')
Then the view function could be defined like this:

def board_topics(request, board_id):
    # do something...
Or like this:

def board_topics(request, id):
    # do something...
The name wouldn’t matter. But it’s a good practice to use named parameters because when we start composing bigger URLs capturing multiple IDs and variables, it will be easier to read.

 Sidenote: PK or ID?

PK stands for Primary Key. It's a shortcut for accessing a model's primary key. All Django models have this attribute.

For the most cases, using the pk property is the same as id. That's because if we don't define a primary key for a model, Django will automatically create an AutoField named id, which will be its primary key.

If you defined a different primary key for a model, for example, let's say the field email is your primary key. To access it you could either use obj.email or obj.pk.


