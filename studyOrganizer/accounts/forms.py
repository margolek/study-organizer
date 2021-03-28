from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateNewUserForm(UserCreationForm):
	#Extend UserCreationForm field (3 default)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)

	class Meta:
		model = User
		fields = ('username','first_name','last_name',
				  'email','password1','password2')

class UpdateProfileImage(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('prof_img')



	



