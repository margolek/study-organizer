from . forms import GroupsModelForm
from . models import Group, GroupMember, GroupRequest
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
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



###################
###Views Methods###
###################

class ListGroup(ListView):
	model = Group

	def get_context_data(self, **kwargs):
		group_request = []
		group = Group.objects.all()
		for i in GroupRequest.objects.all():
			if i.from_user == self.request.user:
				group_request.append(i.group)
		context = super().get_context_data(**kwargs)
		context['group'] = group
		context['group_request'] = group_request
		return context

class SingleGroup(DetailView):
	model = Group

#########################
###Join and Left Group###
#########################

class SendGroupRequest(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:list')

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
		to_user = get_object_or_404(User,id=group.created_by.id)
		try:
			GroupRequest.objects.get_or_create(to_user=to_user,
											   from_user=self.request.user,
											   group=group)
		except:
			messages.warning(self.request,('Warning already a member!'))
		else:
			messages.info(self.request, 'Your request has been sent!')

		return super().get(request,*args,**kwargs)

class CancelGroupRequest(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:list')

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
		to_user = get_object_or_404(User,id=group.created_by.id)
		try:
			group_request = GroupRequest.objects.filter(to_user=to_user,
											   group=group).get()
			group_request.delete()
		except:
			messages.warning(self.request,('You do not remove your group!'))
		else:
			messages.warning(self.request, 'Your request has been removed!')

		return super().get(request,*args,**kwargs)

class AcceptGroupRequest(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('accounts:profile')

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
		to_user = get_object_or_404(User,id=group.created_by.id)
		group_request = GroupRequest.objects.filter(group=group,to_user=to_user).first()
		from_user = group_request.from_user
		try:
			GroupMember.objects.get_or_create(group=group,
											  user=from_user)
			group_request = GroupRequest.objects.filter(to_user=to_user,
											   			group=group,
											   			from_user=from_user).first()
			group_request.delete()			
		except:
			messages.warning(self.request,('Warning already a member!'))
		else:
			messages.success(self.request, f'Request for {from_user}-{group} accepted successfully!')

		return super().get(request,*args,**kwargs)

class RejectGroupRequest(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('accounts:profile')

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
		to_user = get_object_or_404(User,id=group.created_by.id)
		try:
			group_request = GroupRequest.objects.filter(to_user=to_user,
											   group=group).get()
			group_request.delete()			
		except:
			messages.warning(self.request,('User request not found!'))
		else:
			messages.success(self.request, f'You reject user request for group: {group}!')

		return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:list')

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
		try:
			membership = GroupMember.objects.filter(
				user=self.request.user,
				group__slug=self.kwargs.get('slug')).get()

		except models.GroupMember.DoesNotExist:
			messages.warning(self.request, 'Sorry you are not in this group!')

		else:
			membership.delete()
			messages.warning(self.request, f'You are left the group: {group}!')
		return super().get(request,*args,**kwargs)
	



