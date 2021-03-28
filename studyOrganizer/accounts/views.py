from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.shortcuts import redirect


def register(request):
	if request.method == 'POST':
		form = forms.CreateNewUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account Create for {}'.format(username))
			return redirect('index')
	else:
		form = forms.CreateNewUserForm()

	return render(request, 'accounts/register.html',{'form': form})

