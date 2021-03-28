from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	prof_img = models.ImageField(default='default_image.jpg',upload_to='media/profile_pics')
	github_page = models.URLField(max_length=300, blank=True)

	def __str__(self):
		return self.user.username