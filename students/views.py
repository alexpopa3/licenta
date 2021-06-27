from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django import template
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect, reverse
from .forms import QuestionInput, LogInForm, ReasonInput
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Question, Reason, Profile
from django.template import loader
from django.http import HttpResponse, response
from io import StringIO, BytesIO
from xhtml2pdf import pisa
from ultimul import settings

def home(request): 
    return render(request, 'students/home.html')





@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('students:home')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('students:home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'students/change_password.html', {
        'form': form
    })

@login_required
def input_reason(request):
    reason_all = Reason.objects.all().filter(user = request.user)
    if request.method == 'POST':
        reason_form = ReasonInput(request.POST)
        reason = reason_form.save(commit = False)
        reason.user = request.user
        reason.save()
        return redirect('students:certificate')
    else:
        return render(request, 'students/reason.html', {'reason_all': reason_all})


@login_required
def certificate(request):
    reasons = Reason.objects.all().filter(user = request.user).last()
    profiles = Profile.objects.get(user = request.user)
    im = "https://i.ibb.co/gyH7nSM/semnatura.png"
    data = {'reason': reasons,
            'profile': profiles,
            'im' : im,
    }
    
    template = loader.get_template('students/profile.html')
    data_p= template.render(data)
    response = BytesIO()
    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("ISO-8859-1")),response)
    
    return HttpResponse(response.getvalue(),content_type="application/pdf")


@login_required
def input_question(request):
    profile = Profile.objects.get(user = request.user)
    questions = Question.objects.all().filter(user = request.user)
    if request.method == 'POST':
        form = QuestionInput(request.POST)
        question = form.save(commit = False)
        question.user = request.user
        question.question_author = profile.surname + " " + profile.first_name
        question.save()
        return redirect('students:forum')
    else:
        return render(request, 'students/question.html', {'questions': questions})


def view_questions(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.get(user = request.user)
        
        questions = Question.objects.order_by('-posted')
        return render(request, 'students/forum.html', {'questions': questions,  'profiles': profiles})
    else:
        questions = Question.objects.order_by('-posted')
        return render(request, 'students/forum.html', {'questions': questions})

@login_required
def all_mine(request):
    questions = Question.objects.all().filter(user = request.user).order_by('-posted')
    return render(request, 'students/all_mine.html', {'questions': questions})

def detail_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'students/detail.html', {'question': question})

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('students:forum')

@login_required
def delete_question1(request, question_id):
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('students:all_mine')
