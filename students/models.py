from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False,
     default=None, primary_key=True)
    first_name = models.CharField(max_length=20)
    father_initials = models.CharField(max_length=5, blank = True)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank = True)
    phone = models.CharField(max_length=30, blank = True)
    study_year =  models.CharField(max_length=1, blank = True)
    group = models.CharField(max_length=5, blank = True)
    id_number = models.CharField(max_length=10, blank = True, default=None)
    
    def __str__(self):
        return self.user.username

class Reason(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    reason = models.TextField(max_length=300)
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.reason

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.TextField(max_length=1000)
    question_author = models.CharField(max_length=100, default=None)
    answer = models.TextField(max_length=1000, blank=True)
    only_for_me = models.BooleanField(default=False, blank=True)
    anonymous = models.BooleanField(default=False, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    answered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.question)