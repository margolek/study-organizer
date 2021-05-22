from django import forms
from .models import Question,Choice
from groups.models import Group, GroupMember
class QuestionForm(forms.ModelForm):

	choice1 = forms.CharField(label='Choice 1')
	choice2 = forms.CharField(label='Choice 2')

	# def __init__(self, user=None, **kwargs):
	# 	super(QuestionForm, self).__init__(**kwargs)
	# 	if user:
	# 		self.fields['group'].queryset = GroupMember.objects.filter(user=user)
			
	class Meta:
		model = Question
		fields = ['group','question_text','choice1','choice2']
		widgets = {
			'question_text': forms.Textarea(attrs={'class': 'form-control'}),
			'choice1': forms.TextInput(attrs={'class': 'form-control'}),
			'choice2': forms.TextInput(attrs={'class': 'form-control'}),
		}

class EditQuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = ['question_text']
		widgets = {
			'question_text': forms.Textarea(attrs={'class': 'form-control'}),		
		}

class AddChoiceForm(forms.ModelForm):

	class Meta:
		model = Choice
		fields = ['choice_text']
