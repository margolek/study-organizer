from django import forms
from .models import Group, GroupContent, GroupComments

class GroupsModelForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name','description','image']

class GroupContentForm(forms.ModelForm):
	class Meta:
		model = GroupContent
		fields = ['group','topic','context']

class GroupCommentsForm(forms.ModelForm):
	class Meta:
		model = GroupComments
		fields = ['text']