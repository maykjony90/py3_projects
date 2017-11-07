# html'i renderlarmak icin render() fonksiyonunu yukle
from django.shortcuts import render, get_object_or_404, redirect

# bu dosyayla ayni klasorde bulunan models dosyasinin
# icerisindeki 'Board' class'ini yukle 
from .models import Board, Topic, Post

from .forms import NewTopicForm

from django.contrib.auth.models import User



# Burada bir fonkisyon eklediginde urls.py dosyasindan
# URL'i urlpatterns listesine ekle.
# BU SEKMEYE('www.example.com/home' or 'www.example.com/'') 
# BIR 'REQUEST' GELDIGINDE HOME() FONKSIYONUNU CALISTIR  
def home(request):
	# BOARDS/OBJECTS DOSYASINDAN BUTUN OBJELERI GETIR.
	boards = Board.objects.all()
	# request(istegi)'i, templates/home.html dosyasini ve
	# html dosyasinin icindeki 'boards' degiskenleri icin 'boards' objesini kullan
	return render(request, 'home.html', { 'boards':boards })


# Primary Key'i verilen URL'e request alir.
# The regex \d+ will match an integer of arbitrary size. This integer will be used 
# to retrieve the Board from the database. Now observe that we wrote the 
# regex as (?P<pk>\d+), this is telling Django to capture the value into 
# a keyword argument named pk.
def board_topics(request, pk):
	# Yukaridakilere gerek kalmadan shortcuts'tan get_object_or_404
	# cagirip kullanabiliriz.
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'topics.html', {'board':board})


def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	user = User.objects.first()  # TODO: get the currently logged in user

	# First we check if the request is a POST or a GET. If the request came from a POST,
	#  it means the user is submitting some data to the server. So we instantiate 
	#  a form instance passing the POST data to the form:
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		# we ask Django to verify the data, check if the form is valid if we can 
		# save it in the database: if form.is_valid():. If the form was valid, 
		# we proceed to save the data in the database using form.save(). 
		# The save() method returns an instance of the Model saved into the database. 
		# So, since this is a Topic form, it will return the Topic that was created: 
		# topic = form.save(). After that, the common path is to redirect the user 
		# somewhere else, both to avoid the user re-submitting the form by pressing F5 
		# and also to keep the flow of the application.
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = user
			topic.save()
			post = Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=user
				)
			return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
	# If the request was a GET, we just initialize a new and empty form using 
	# form = NewTopicForm().
	else:
		form = NewTopicForm()

	return render(request, 'new_topic.html', {'board': board, 'form': form})