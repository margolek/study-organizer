from . forms import GroupsModelForm
from . models import Group, GroupMember
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


#########################
###Join and Left Group###
#########################

class JoinGroup(LoginRequiredMixin,generic.base.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:list')

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

		try:
			GroupMember.objects.create(user=self.request.user,group=group)
		except:
			messages.warning(self.request,('Warning already a member!'))
		else:
			messages.success(self.request, f'You are now a member of group: "{group}"!')

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
	



