from django.db import models
from django.contrib.auth.models import User
import secrets

class Question(models.Model):
	# created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	# active = models.BooleanField(default=True)

	# def user_can_vote(self, user):
	# 	""" 
	# 	Return False if user already voted
	# 	"""
	# 	user_votes = user.vote_set.all()
	# 	qs = user_votes.filter(poll=self)
	# 	if qs.exists():
	# 		return False
	# 	return True

	# @property
	# def get_vote_count(self):
	# 	return self.vote_set.count()

	# def get_result_dict(self):
	# 	res = []
	# 	for choice in self.choice_set.all():
	# 		d = {}
	# 		alert_class = ['primary', 'secondary', 'success',
	# 					   'danger', 'dark', 'warning', 'info']
	# 		d['alert_class'] = secrets.choice(alert_class)
	# 		d['text'] = choice.choice_text
	# 		d['num_votes'] = choice.get_vote_count
	# 		if not self.get_vote_count:
	# 			d['percentage'] = 0
	# 		else:
	# 			d['percentage'] = (choice.get_vote_count /self.get_vote_count)*100
	# 		res.append(d)
	# 	return res

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	# @property
	# def get_vote_count(self):
	# 	return self.vote_set.count()

	def __str__(self):
		return self.choice_text

# class Vote(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	question = models.ForeignKey(Question, on_delete=models.CASCADE)
# 	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return f'{self.poll.text[:15]},{self.user.username}'
