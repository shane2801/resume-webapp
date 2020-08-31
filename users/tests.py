from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from blog.models import Post
from users.models import Profile
import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from os import unlink
from tempfile import NamedTemporaryFile
from users import signals


class TestModels(TestCase):


	def setUp(self):
		# Every test needs access to the request factory.
		self.factory = RequestFactory()
		self.client = Client()
		self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		self.client.login(username='john', password='johnpassword')
		#newPhoto = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
		image = Image.new('RGB', (100, 100))
		image_file = NamedTemporaryFile(suffix='.jpg')
		image.save(image_file)
		self.client.login(username='john', password='johnpassword')
		Profile.objects.create(
			user = self.user,
			image=image_file,
			address='birmingham',
			phone_number='9876',
			personal_profile='student',
			education='BSc',
			experience='none',
			skills='IT',
			languages='french',
			other_relevant_experience='projects',
			referrences='doonoah')

	def test_address_profile(self):
		profile = Profile.objects.get(id=1)
		expected_address = f'{profile.address}'
		self.assertEquals(expected_address, 'birmingham')