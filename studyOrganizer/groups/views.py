from django.shortcuts import render
from . forms import GroupsModelForm,GroupContentForm,GroupCommentsForm
from . models import Group,GroupContent,GroupComments
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

@login_required
def create_group_content(request,pk):
	group = get_object_or_404(Group, pk=pk)
	user = request.user
	if request.method == 'POST':
		form = GroupContentForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.instance.author = user
			form.instance.group = group
			form.save()
			messages.success(request, f'Posted successfully')
			return redirect('groups:detail', pk=pk)
	else:
		form = GroupContentForm()
	return render(request,'groups/content_form.html',{'group':group,'form':form})


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

# class GroupContentUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
# 	model = GroupContent
# 	form_class = GroupContentForm
# 	template_name = 'groups/content_form.html'

# 	def get_context_data(self,**kwargs):
# 		context = super().get_context_data()
# 		post_id = GroupContent.objects.get(id=self.kwargs.get('post_id', ''))
# 		context['post_id'] = post_id
# 		return context


# 	def form_valid(self,form):
# 		form.instance.author = self.request.user
# 		return super().form_valid()

# 	def test_func(self):
# 		group_content = self.get_object()
# 		if self.request.user == group_content.author:
# 			return True
# 		return False

class GroupContentDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = GroupContent
	success_url = 'groups:list'

	def test_func(self):
		group_content = self.get_object()
		if self.request.user == group_content.author:
			return True
		return False

###################
###Views Methods###
###################

class ListGroup(ListView):
	model = Group
	context_object_name = 'group'

class SingleGroup(DetailView):
	model = Group

class GroupContentDetailView(DetailView):
	model = GroupContent
	template_name = 'groups/content_detail.html'
	context_object_name = 'group_content'
	



