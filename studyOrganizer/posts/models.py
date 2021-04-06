from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class GroupContent(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='groupacc')
	topic = models.CharField(max_length=100)	
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='group')
	context = models.TextField(max_length=1000)
	creation_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.topic

	def get_abolute_url(self):
		return reverse('groups:detail',kwargs={'pk':self.pk})

class GroupComments(models.Model):
	group_content = models.ForeignKey(GroupContent, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
	date = models.DateTimeField(default=timezone.now)
	text = models.CharField(max_length=256)

