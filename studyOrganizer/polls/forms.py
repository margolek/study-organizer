from django import forms
from .models import Question,Choice

class QuestionForm(forms.ModelForm):

	choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=2)
	choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=2)

	class Meta:
		model = Question
		fields = ['question_text','choice1','choice2']
		widgets = {
			'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
			'choice1': forms.TextInput(attrs={'class': 'form-control'}),
			'choice2':forms.TextInput(attrs={'class': 'form-control'}),
		}

class EditQuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = ['question_text']
		widgets = {
			'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
		}

class AddQuestionChoice(forms.ModelForm):

	class Meta:
		model = Choice
		fields = ['choice_text']
		widgets = {
			'choice_text': forms.TextInput(attrs={'class': 'form-control', })
		}		
