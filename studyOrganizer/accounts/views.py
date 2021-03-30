from django.shortcuts import render
from .forms import (CreateNewUserForm, UpdateProfileImage,
					UpdateProfileInfo)
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required



def register(request):
	if request.method == 'POST':
		form = CreateNewUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account Create for {}'.format(username))
			return redirect('index')
	else:
		form = CreateNewUserForm()

	return render(request, 'accounts/register.html',{'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		form_info = UpdateProfileInfo(request.POST)
		if form_info.is_valid():
			form_info.save()
			messages.success(request, 'Profile picture updated successfully!')
			return redirect('index')
	else:
		form_info = UpdateProfileInfo(instance=request.user)

	my_dict = {
		'form_info':form_info
	}

	return render(request, 'accounts/profile.html',my_dict)





