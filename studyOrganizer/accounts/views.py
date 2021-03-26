from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic.edit import CreateView

class RegisterUser(CreateView):
	form_class = forms.CreateNewUserForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/register.html'
