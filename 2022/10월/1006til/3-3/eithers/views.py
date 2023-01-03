from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseForbidden
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
import random

def index(request):
    eithers = Question.objects.all()
    context = {
        'eithers': eithers,
    }
    return render(request, 'eithers/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            either = form.save()
            return redirect('eithers:index')
        
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)

def detail(request, pk):
    either = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = either.comment_set.all()
    context = {
        'either': either,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    either = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=either)
        if form.is_valid():
            form.save()
            return redirect('eithers:detail', either.pk)
    else:
        form = QuestionForm(instance=either)
    context = {
        'form': form,
        'either': either,
    }
    return render(request, 'eithers/update.html', context)


@require_POST
def comments_create(request, pk):
    either = Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = either
        comment.save()
        return redirect('eithers:detail', either.pk)
    return redirect('eithers:detail', either.pk)

def random_2(request):
    possible_list = Question.objects.all()
    selected_page = random.choice(possible_list)
    return redirect('eithers:detail', selected_page.pk)

@require_POST
def delete(request, pk):
    either = Question.objects.get(pk=pk)
    
    either.delete()
    return redirect('eithers:index')
    
