from django import forms
from .models import Group

class GroupsModelForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name','description','image']


# class GroupContentForm(ModelForm):
#     class Meta:
#         model = GroupContent
#         exclude = ()

# 	FamilyMemberFormSet = inlineformset_factory(Group, GroupContent,
#                                             form=GroupContentForm, extra=1)