from django.shortcuts import render
from . forms import GroupsModelForm,GroupContentForm,GroupCommentsForm
from . models import Group,GroupContent,GroupComments
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
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
def create_group_content(request):
	user = request.user
	if request.method == 'POST':
		form = GroupContentForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.instance.author = user
			form.save()
			messages.success(request, f'Posted successfully')
			return redirect('groups:content_view')
	else:
		form = GroupContentForm()
	return render(request,'groups/content_form.html',{'form':form})

class GroupContentUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = GroupContent
	fields = ['topic','context']
	template_name = 'groups/content_form.html'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid()

	def test_func(self):
		group_content = self.get_object()
		if self.request.user == group_content.author:
			return True
		return False

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

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['post_lists'] = GroupContent.objects.all()
		return context

# class GroupContentView(ListView):
# 	model = GroupContent
# 	template_name = 'groups/content_list.html'
# 	context_object_name = 'group_content'
# 	ordering = ['-creation_date']



