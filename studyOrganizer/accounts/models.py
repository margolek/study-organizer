from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django_resized import ResizedImageField



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	prof_img = models.ImageField(default='profile_pics/default_man.jpg',upload_to='profile_pics')
	github_page = models.URLField(max_length=300, blank=True)
	birth_date = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.user.username






