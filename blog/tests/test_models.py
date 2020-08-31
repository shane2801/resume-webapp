from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from blog.models import Post
from users.models import Profile
import datetime
from django.core.files.uploadedfile import SimpleUploadedFile

class TestModels(TestCase):


	def setUp(self):
		# Every test needs access to the request factory.
		self.factory = RequestFactory()
		self.user = User.objects.create_user(
			username='jacob', email='jacob@gmail.com', password='top_secret')
		Post.objects.create(title='tdd',content='tedious',date_posted= datetime.date(2010, 1, 1),author=self.user)

	#tests whether the field title of our blog works
	def test_title(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'title')
	#tests if the blog's content field is accurate
	def test_content(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('content').verbose_name
		self.assertEquals(field_label, 'content')
	#checks if the blog's date posted field works as inteded
	def test_content(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('date_posted').verbose_name
		self.assertEquals(field_label, 'date posted')
	#cchecks the post title if its accurate
	def test_title_post_and_dunder_method(self):
		post = Post.objects.get(id=1)
		expected_title = f'{post.title}'
		self.assertEquals(expected_title, str(post))
	#checks if the post content is accurate
	def test_content_post(self):
		post = Post.objects.get(id=1)
		expected_content = f'{post.content}'
		self.assertEquals(expected_content, 'tedious')

	def setUpProfile(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='jacob1', email='jacob1@gmail.com', password='top_secret1')
		newPhoto = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')

		Profile.objects.create(username=self.user,
			image=newPhoto,
			address='birmingham',
			phone_number='9876',
			personal_profile='student',
			education='BSc',
			experience='none',
			skills='IT',
			languages='french',
			other_relevant_experience='projects',
			referrences='doonoah')
		
	#testing the fields of the profile model

	def test_address(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('address').verbose_name
		self.assertEquals(field_label, 'address')
	
	def test_phone_number(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('phone_number').verbose_name
		self.assertEquals(field_label, 'phone number')

	def test_personal_profile(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('personal_profile').verbose_name
		self.assertEquals(field_label, 'personal profile')

	def test_educatioon(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('education').verbose_name
		self.assertEquals(field_label, 'education')

	def test_experience(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('experience').verbose_name
		self.assertEquals(field_label, 'experience')

	def test_skills(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('skills').verbose_name
		self.assertEquals(field_label, 'skills')

	def test_languages(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('languages').verbose_name
		self.assertEquals(field_label, 'languages')

	def test_other(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('other_relevant_experience').verbose_name
		self.assertEquals(field_label, 'other relevant experience')

	def test_referrences(self):
		post = Profile.objects.get(id=1)
		field_label = Profile._meta.get_field('referrences').verbose_name
		self.assertEquals(field_label, 'referrences')

	#testing the content of the profile model fields

	def test_username_and_dunder_method(self):
		profile = Profile.objects.get(id=1)
		expected_username = f'{profile.username}'
		self.assertEquals(expected_username, str(username))
	
	def test_address_profile(self):
		profile = Profile.objects.get(id=1)
		expected_address = f'{profile.address}'
		self.assertEquals(expected_address, 'birmingham')

	def test_phonenum_profile(self):
		profile = Profile.objects.get(id=1)
		expected_num = f'{profile.phone_number}'
		self.assertEquals(expected_address, '9876')

	def test_pp_profile(self):
			profile = Profile.objects.get(id=1)
			expected_pp = f'{profile.personal_profile}'
			self.assertEquals(expected_pp, 'student')

	def test_education_profile(self):
			profile = Profile.objects.get(id=1)
			expected = f'{profile.education}'
			self.assertEquals(expected, 'BSc')
	
	def test_experience_profile(self):
			profile = Profile.objects.get(id=1)
			expected_address = f'{profile.experience}'
			self.assertEquals(expected, 'none')

	def test_skills_profile(self):
			profile = Profile.objects.get(id=1)
			expected = f'{profile.skills}'
			self.assertEquals(expected, 'IT')
	
	def test_languages_profile(self):
			profile = Profile.objects.get(id=1)
			expected_languages = f'{profile.languages}'
			self.assertEquals(expected_languages, 'french')
	
	def test_other_profile(self):
			profile = Profile.objects.get(id=1)
			expected = f'{profile.other_relevant_experience}'
			self.assertEquals(expected, 'projects')

	def test_referrences_profile(self):
			profile = Profile.objects.get(id=1)
			expected = f'{profile.referrences}'
			self.assertEquals(expected, 'doonoah')







