from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
# from groups.models import GroupMember,Group

#We hook two methods to the User model, whenever a save event occurs. This is called 'post_save' signal

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance,created, **kwargs):
	if created == False:
		instance.profile.save()
