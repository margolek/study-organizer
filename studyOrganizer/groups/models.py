from django.db import models
from django.urls import reverse
from django.utils import timezone


from django.contrib.auth import get_user_model
User = get_user_model()

class Group(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=300)
	image = models.ImageField(blank=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE,
								   related_name='author')
	members = models.ManyToManyField(User,related_name='members')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('groups:detail', kwargs={'pk':self.pk})

	class Meta:
		ordering = ['name']






