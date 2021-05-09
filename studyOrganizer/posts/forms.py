from django import forms
from .models import Content, Comments
from django.utils.translation import gettext_lazy as _

class ContentForm(forms.ModelForm):
	class Meta:
		model = Content
		fields = ['topic','context']

class CommentsForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['text']
		widgets = {
			'text': forms.TextInput(attrs={'placeholder': 'Type your comment',}),
		}

