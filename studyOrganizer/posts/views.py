from . forms import ContentForm,CommentsForm
from . models import Content,Comments
from groups.models import Group
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User

@login_required
def create_content(request,slug):
	group = get_object_or_404(Group, slug=slug)
	user = request.user
	if request.method == 'POST':
		form = ContentForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.instance.author = user
			form.instance.group = group
			form.save()
			messages.success(request, f'Posted successfully')
			return redirect('groups:detail', slug=slug)
	else:
		form = ContentForm()
	return render(request,'posts/content_form.html',{'group':group,'form':form})

@login_required
def content_detail(request,pk):
	group_content = get_object_or_404(Content,pk=pk)
	author = request.user
	if request.method == 'POST':
		form = CommentsForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.instance.group_content = group_content
			form.instance.author = author
			form.save()
			return redirect('posts:detail',pk=pk)
	else:
		form = CommentsForm()
	return render(request, 'posts/content_detail.html',{'group_content':group_content,'form':form})

class ContentUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
	model = Content
	form_class = ContentForm
	template_name = 'posts/update_form.html'
	success_message = 'Post Updated successfully'

	def form_valid(self,form):
		form.instance.author = self.request.user
		form.instance.group = Group.objects.get(slug=self.kwargs['slug'])
		return super().form_valid(form)

	def test_func(self):
		group_content = self.get_object()
		if self.request.user == group_content.author:
			return True
		return False

	def get_success_url(self):
		groupslug=self.kwargs['slug']
		return reverse_lazy('groups:detail', kwargs={'slug':groupslug})

class ContentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Content

	def get_success_url(self):
		# in order to pass 'slug' from 'urls' to 'DeleteView'
		# capture that 'slug' as groupslug and pass it to 'reverse_lazy()' function
		groupslug=self.kwargs['slug']
		return reverse_lazy('groups:detail', kwargs={'slug':groupslug})

	def test_func(self):
		post_obj = self.get_object()
		if self.request.user == post_obj.author:
			return True
		return False

