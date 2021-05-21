from django import forms
from .models import Question,Choice

class QuestionForm(forms.ModelForm):

	choice1 = forms.CharField(label='Choice 1')
	choice2 = forms.CharField(label='Choice 2')

	class Meta:
		model = Question
		fields = ['question_text','choice1','choice2']
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
