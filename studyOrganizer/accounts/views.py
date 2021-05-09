from django.shortcuts import render
from . forms import (CreateNewUserForm, UpdateProfileImage,
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
			return redirect('accounts:login')
	else:
		form = CreateNewUserForm()

	return render(request, 'accounts/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateProfileInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account update successfully')
            return redirect('accounts:profile')

    else:
        form = UpdateProfileInfo(instance=request.user)
        
    return render(request, 'accounts/profile.html', {'form':form})





