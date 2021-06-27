from django import forms
from .models import Group, GroupMember

class GroupsModelForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name','description','image']
