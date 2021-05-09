from . forms import GroupsModelForm
from . models import Group
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User


########################################
###Creating/Updating/Deleting Methods###
########################################

@login_required
def creategroup(request):
	if request.method == 'POST':
		form = GroupsModelForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.instance.created_by = request.user
			form.save()
			messages.success(request, message='New group created successfully')
			return redirect('groups:list')
	else:
		form = GroupsModelForm()

	return render(request, 'groups/group_form.html',{'form':form})


# def update_group_content(request,pk,post_id)

# 	group = get_object_or_404(Group,pk=pk)
# 	content = get_object_or_404(GroupComments,pk=post_id)
# 	form = GroupContentForm()
# 	post_id = GroupContentForm.objects.get(id=self.kwargs.get('post_id', ''))
#         context['page_alt'] = page_alt
# 	context = {
# 		'form':form
# 	}
# 	return render(request, 'groups/content_form.html',context)





###################
###Views Methods###
###################

class ListGroup(ListView):
	model = Group
	context_object_name = 'group'

class SingleGroup(DetailView):
	model = Group

# class GroupContentDetailView(DetailView):
# 	model = GroupContent
# 	template_name = 'groups/content_detail.html'
# 	context_object_name = 'group_content'
	



