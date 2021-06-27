from django.db import models
from django.urls import reverse
from django.utils import timezone
from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Content(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='groupacc')
	topic = models.CharField(max_length=100)	
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='group')
	context = models.TextField(max_length=1000)
	creation_date = models.DateTimeField(editable=False)
	updated_date = models.DateTimeField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.creation_date = timezone.now()
		self.updated_date= timezone.now()
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.topic

	def get_abolute_url(self):
		return reverse('groups:detail',kwargs={'pk':self.pk})

class Comments(models.Model):
	group_content = models.ForeignKey(Content, on_delete=models.CASCADE,related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
	date = models.DateTimeField(default=timezone.now)
	text = models.CharField(max_length=256,verbose_name='Comment')

class Super(models.Model):
	user = models.ForeignKey(User,related_name='supers',on_delete=models.CASCADE)
	post = models.ForeignKey(Content,related_name='supers', on_delete=models.CASCADE)

	def __str__(self):
		return f'user:{self.user},post:{self.post}'

class Like(models.Model):
	user = models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
	post = models.ForeignKey(Content,related_name='likes', on_delete=models.CASCADE)

	def __str__(self):
		return f'user:{self.user},post:{self.post}'

class Dislike(models.Model):
	user = models.ForeignKey(User,related_name='dislikes',on_delete=models.CASCADE)
	post = models.ForeignKey(Content,related_name='dislikes', on_delete=models.CASCADE)

	def __str__(self):
		return f'user:{self.user},post:{self.post}'