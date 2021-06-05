from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Question, Choice, Vote
from .forms import QuestionForm, EditQuestionForm, AddChoiceForm
from groups.models import Group
from django.template.defaulttags import register


@login_required
def create_polls(request):
    if request.method == 'POST':
        form = QuestionForm(user=request.user,data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.pub_date = timezone.now()
            question.save()
            new_choice1 = Choice(
                question=question, choice_text=form.cleaned_data['choice1']).save()
            new_choice2 = Choice(
                question=question, choice_text=form.cleaned_data['choice2']).save()
            messages.success(request, message='New Poll created successfully')
            return redirect('polls:index')
    else:
        form = QuestionForm(user=request.user)

    return render(request, 'polls/polls_form.html',{'form':form})

# Update Poll question
class PollUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Question
    form_class = EditQuestionForm
    template_name = 'polls/update_question.html'
    success_message = 'Question Updated successfully'
    success_url = reverse_lazy('polls:index')

        

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.created_by and (self.request.user in question.group.members.all()):
            return True
        return False

# Delete existing poll
class PollDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.created_by and (self.request.user in question.group.members.all()):
            return True
        return False

@login_required
def add_choice(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.user != question.created_by:
        return redirect('polls:index')

    if request.method == 'POST':
        form = AddChoiceForm(request.POST)
        if form.is_valid:
            new_choice = form.save(commit=False)
            new_choice.question = question
            new_choice.save()
            messages.success(request, "Choice added successfully")
            return redirect('polls:index')
    else:
        form = AddChoiceForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/add_choice.html', context)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def index(request):
    permissions = {}
    question_list = Question.objects.order_by('-pub_date')
    for i in question_list:
        permissions[i.question_text] = i.voting_permission(request.user)
    print(permissions)
    paginator = Paginator(question_list, 10)
    page = request.GET.get('page')
    question_list = paginator.get_page(page)
    context = {'question_list': question_list,
               'permissions':permissions}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, pk):
  try:
    question = Question.objects.get(pk=pk)
    if not question.group_permission(request.user):
        messages.warning(request, "Permission denied!")
        return redirect("polls:index")
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if not question.group_permission(request.user):
        messages.warning(request, "Permission denied!")
        return redirect("polls:index")
    return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        if not question.voting_permission(request.user):
            messages.warning(request, "You already voted this poll !")
            return redirect("polls:index")
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        vote = Vote(user=request.user, question=question, choice=selected_choice)
        vote.save()
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)



