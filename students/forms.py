from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import Profile, Reason, Question

class LogInForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'password']
      widgets= {
         'username': forms.TextInput(attrs={'class': 'form-control'}),
         'password': forms.TextInput(attrs={'class': 'form-control'}),
         
      }


class ReasonInput(forms.ModelForm):   
   class Meta:
      model = Reason
      fields = ['reason', ]
      widgets= {
         'reason': forms.Textarea(attrs={'class': 'form-control'}),
      }

class QuestionInput(forms.ModelForm):
   class Meta:
      model = Question
      fields = ['question', 'only_for_me', 'anonymous']
      widgets= {
         'question': forms.Textarea(attrs={'class': 'form-control'}),
         'only_for_me': forms.CheckboxInput(attrs={'class': 'form-control'}),
         'anonymous': forms.CheckboxInput(attrs={'class': 'form-control'}),
      }