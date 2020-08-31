from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import home,resume
from users.views import register, profile

class TestUrls(TestCase): 

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