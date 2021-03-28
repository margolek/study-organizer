from django.shortcuts import render
from .forms import CreateNewUserForm, UpdateProfileImage
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required



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

@login_required
def profile(request):
	if request.method == 'POST':
		form = UpdateProfileImage(request.POST, request.FILES,instance=request.user.profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile picture updated successfully!')
			return redirect('index')
	else:
		form = UpdateProfileImage()
	return render(request, 'accounts/profile.html',{'form':form})





