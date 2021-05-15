from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


from django.contrib.auth import get_user_model
User = get_user_model()

class Group(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(allow_unicode=True,unique=True,default='')
	description = models.TextField(max_length=300)
	image = models.ImageField(blank=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE,
								   related_name='author')
	members = models.ManyToManyField(User,related_name='members',through='GroupMember')

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super().save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('groups:detail', kwargs={'pk':self.pk})

	class Meta:
		ordering = ['name']

class GroupMember(models.Model):
	group = models.ForeignKey(Group,related_name='membership',
							  on_delete=models.CASCADE)
	user = models.ForeignKey(User,related_name='user_group',
							 on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		unique_together = ['group','user']






