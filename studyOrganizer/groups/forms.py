from django import forms
from .models import Group, GroupContent, GroupComments

class GroupsModelForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name','description','image']

class GroupContentForm(forms.ModelForm):
	class Meta:
		model = GroupContent
		fields = ['topic','context']

class GroupCommentsForm(forms.ModelForm):
	class Meta:
		model = GroupComments
		fields = ['text']

# class GroupContentForm(ModelForm):
#     class Meta:
#         model = GroupContent
#         exclude = ()

# 	FamilyMemberFormSet = inlineformset_factory(Group, GroupContent,
#                                             form=GroupContentForm, extra=1)