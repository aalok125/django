from django.http import HttpResponse
from django.shortcuts import redirect
from .models import GuestUser, UserVote, Question
import requests

#function to check if user has previously attempted question   
def attempt_check(view_func):
    def wrapper_func(request,*args, **kwargs):
        guest_id = request.session.get('guest_user')
        guest = GuestUser.objects.get(pk=guest_id)
        question = Question.objects.get(slug = kwargs.get('question_slug')) 
        if (guest.uservote_set.filter(question = question)).exists():
            return redirect('result',question.slug)
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

