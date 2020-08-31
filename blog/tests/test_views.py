from django.test import TestCase, Client
from django.urls import reverse, resolve
from users.views import register, profile
from django.contrib.auth.models import User

class TestViews(TestCase):

	def test_home_GET(self):
		client = Client()
		response = client.get(reverse('blog-home'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'blog/home.html')

	def test_resume_GET(self):
		client = Client()
		response = client.get(reverse('resume'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'blog/resume.html')

	def test_register_GET(self):
		client = Client()
		response = client.get(reverse('register'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'users/register.html')

	#testing the login process as you need you are redirected to a login page before you are allowed to access the profile
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

	def test_profile_GET(self):
		self.client.login(username='john', password='johnpassword')
		response = self.client.get(reverse('profile'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'users/profile.html')