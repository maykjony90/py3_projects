from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
# ayni klasordeki view dosyasindan naber foksiyonunu cagir
from .views import home, board_topics, new_topic
from .models import Board, Topic, Post
from .forms import NewTopicForm


"""
Siteyi calistirmadan once bazi testler yurutmek oldukca
mantikli bir davranis olur.
"""

# '/home' yada '/', yani acilis sayfasini test eden class
class HomeTests(TestCase):
	def setUp(self):
		self.board = Board.objects.create(name='Django', description='Django board.')
		url = reverse('home')
		self.response = self.client.get(url)


	def test_home_view_status_code(self):
		self.assertEquals(self.response.status_code, 200)


	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)

	# The new test here is the test_home_view_contains_link_to_topics_page. 
	# Here we are using the assertContains method to test if the response 
	# body contains a given text. The text we are using in the test, 
	# is the href part of an a tag. So basically we are testing 
	# if the response body has the text href="/boards/1/".
	def test_home_view_contains_link_to_topics_page(self):
		board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
		self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))



# Board a ait olan topicleri test eden class.
class BoardTopics(TestCase):
	def setUp(self):
		Board.objects.create(name='Django', description='Django board.')

	# Bu fonksiyon icinde gecen pk, Primary Key. pk:1, yukarida yarattigimiz
	# objenin ID numarasi. 1 numarali obje var oldugu icin bu fonksiyondaki
	# status code'un 200 olarak donus yapmasini bekliyoruz.
	def test_board_topics_view_succes_status_code(self):
		url = reverse('board_topics', kwargs={'pk':1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)


	# Var olmayan bir sayfa cagirilmak istendiginde dogru bir bicimde
	# 404 status code'u donus yapiyor mu diye kontrol et
	def test_board_topics_view_not_found_status_code(self):
		url = reverse('board_topics', kwargs={'pk':99})
		response = self.client.get(url)
		# Eger status code 404 ise OK olarak donus yapar
		self.assertEquals(response.status_code, 404)


	# tests if django is using the correct view function to render the topics
	def test_board_topics_url_resolvers_board_topics_view(self):
		view = resolve('/boards/1/')
		self.assertEquals(view.func, board_topics)


	def test_board_topics_view_contains_navigation_links(self):
		board_topics_url = reverse('board_topics', kwargs={'pk':1})
		homepage_url = reverse('home')
		new_topic_url = reverse('new_topic', kwargs={'pk': 1})

		response = self.client.get(board_topics_url)

		self.assertContains(response, 'href="{0}"'.format(homepage_url))
		self.assertContains(response, 'href="{0}"'.format(new_topic_url))







class NewTopicTests(TestCase):
	def setUp(self):
		Board.objects.create(name='Django', description='Django board.')

	# Bu fonksiyon icinde gecen pk, Primary Key. pk:1, yukarida yarattigimiz
	# objenin ID numarasi. 1 numarali obje var oldugu icin bu fonksiyondaki
	# status code'un 200 olarak donus yapmasini bekliyoruz.
	def test_new_topic_view_succes_status_code(self):
		url = reverse('new_topic', kwargs={'pk':1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)


	# Var olmayan bir sayfa cagirilmak istendiginde dogru bir bicimde
	# 404 status code'u donus yapiyor mu diye kontrol et
	def test_new_topic_view_not_found_status_code(self):
		url = reverse('board_topics', kwargs={'pk':99})
		response = self.client.get(url)
		# Eger status code 404 ise OK olarak donus yapar
		self.assertEquals(response.status_code, 404)


	# tests if django is using the correct view function to render the topics
	def test_new_topic_url_resolvers_new_topic_view(self):
		view = resolve('/boards/1/new/')
		self.assertEquals(view.func, new_topic)


	def test_new_topic_view_contains_link_back_to_board_topics_view(self):
		new_topic_url = reverse('new_topic', kwargs={'pk':1})
		board_topics_url = reverse('board_topics', kwargs={'pk':1})
		response = self.client.get(new_topic_url)
		self.assertContains(response, 'href="{0}"'.format(board_topics_url))

	# test_csrf: since the CSRF Token is a fundamental part of 
	# processing POST requests, we have to make sure our HTML contains the token.
	def test_csrf(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.get(url)
		self.assertContains(response, 'csrfmiddlewaretoken')


	def test_new_topic_valid_post_data(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		data = {
			'subject': 'Test Title',
			'message': "Lorem Ipsum dolor sit amet"
		}
		response = self.client.post(url, data)
		self.assertTrue(Topic.objects.exists())
		self.assertTrue(Post.objects.exists())


	# test_new_topic_valid_post_data: sends a valid combination of data 
	# and check if the view created a Topic instance and a Post instance.
	def test_new_topic_invalid_post_data(self):
		"""
		Invalid post data should not redirect
		The expected behavior is to show the form again with validation errors.
		"""
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.post(url, {})
		self.assertEquals(response.status_code, 200)


	# test_new_topic_invalid_post_data_empty_fields: similar to the previous test, 
	# but this time we are sending some data. The application is expected to 
	# validate and reject empty subject and message.
	def test_new_topic_invalid_post_data_empty_fields(self):
		"""
		Invalid post data should not redirect
		The expected behavior is to show the form again with validation errors.
		"""
		url = reverse('new_topic', kwargs={'pk': 1})
		data = {
			'subject': '',
			'message': ''
		}
		response = self.client.post(url, data)
		self.assertEquals(response.status_code, 200)
		self.assertFalse(Topic.objects.exists())
		self.assertFalse(Post.objects.exists())


	# Now we are using the assertIsInstance method for the first time. 
	# Basically we are grabbing the form instance in the context data, 
	# and checking if it is a NewTopicForm.
	def test_contains_form(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.get(url)
		form = response.context.get('form')
		self.assertIsInstance(form, NewTopicForm)


	# In the last test, we added the self.assertTrue(form.errors) to make sure 
	# the form is showing errors when the data is invalid.
	def test_new_topic_invalid_post_data(self):
		'''
		Invalid post data should not redirect
		The expected behavior is to show the form again with validation errors.
		'''
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.post(url, {})
		form = response.context.get('form')
		self.assertEquals(response.status_code, 200)
		self.assertTrue(form.errors)


