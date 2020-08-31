from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import home, resume
from users.views import register, profile
from django.contrib.auth.models import User
import json

class MyTests(TestCase):

#testing urls of our website
	def test_home_url_is_resolved(self):
		url = reverse('blog-home')
		self.assertEquals(resolve(url).func,home)

	def test_resume_url_is_resolved(self):
		url = reverse('resume')
		self.assertEquals(resolve(url).func,resume)
	
	def test_register_url_is_resolved(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func,register)

	def test_profile_url_is_resolved(self):
		url = reverse('profile')
		self.assertEquals(resolve(url).func,profile)

#testing views of our website
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

	#testing the login process as you need to before accessing the profile
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

	def test_profile_GET(self):
		self.client.login(username='john', password='johnpassword')
		response = self.client.get(reverse('profile'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'users/profile.html')