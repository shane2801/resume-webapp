from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default = 'default.jpg',upload_to='profile_pics')
	address = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)
	personal_profile = models.TextField()
	education = models.TextField()
	experience = models.TextField()
	skills = models.TextField()
	languages = models.TextField()
	other_relevant_experience = models.TextField()
	referrences = models.TextField()

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,*args, **kawrgs):
		super().save(*args, **kawrgs)

		img = Image.open(self.image.path)

		if img.height> 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


