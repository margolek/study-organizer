from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	prof_img = ResizedImageField(size=[100,100],default='default_man.jpg',upload_to='profile_pics')
	github_page = models.URLField(max_length=300, blank=True)
	birth_date = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.user.username




