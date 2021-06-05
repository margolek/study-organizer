from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Question(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE,default='',null=True)
	group = models.ForeignKey(Group, on_delete=models.CASCADE,default='',null=True)
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def voting_permission(self,user):
		"""
		False if user already voted
		"""
		vote = user.vote_set.all()
		q = vote.filter(question=self)
		if q.exists():
			return False
		return True

	def group_permission(self,user):
		"""
		False if user not in group
		"""
		if user in self.group.members.all():
			return True
		return False

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'question:{self.question.question_text[:10]},username:{self.user.username}'
