from django.shortcuts import render, HttpResponse, Http404
from django.views import View
from .models import *
from random import randint
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
# def index(request):
#     return HttpResponse("hello")

class HomeView(View):
    template_name = "front/index.html"
    def get(self, request):
        categories = Category.objects.filter(parent=None)
        for category in categories:
            category.active = True
            break
        count = Question.objects.count()
        trending_question = Question.objects.all()[randint(0, count - 1)]
        trending_question.answers = trending_question.answer_set.all()[:5]
        dictionary = {
            'categories':categories,
            'trending_question':trending_question,
        }
        return render(request,self.template_name, context=dictionary)


class CategoryView(View):
    template_name="front/category.html"
    def get(self, request, category_slug):
        try:
            category = Category.objects.get(slug=category_slug)
            dictionary = {
                'category':category
            }
        except Category.DoesNotExist:
            raise Http404
        return render(request,self.template_name,context=dictionary)

class PollPageView(View):
    template_name = "front/votingPage.html"
    def get(self, request, question_slug):
        try:
            question = Question.objects.get(slug=question_slug)
            dictionary = {
                'question':question
            }
        except Question.DoesNotExist:
            raise Http404
        return render(request,self.template_name, context=dictionary)

class VoteSelectView(View):
    def get(self, request, question_slug, answer_pk):
        return HttpResponse(question_slug+""+answer_pk)

class PollResultView(View):
    template_name = "front/votingResult.html"
    def get(self, request):
        context = {}
        return render(request,self.template_name)

def filter_options(request, question_slug):
    try:
        question = Question.objects.get(slug=question_slug)
        search = request.POST['search_text']
        if(search == ""):
            answers = question.answer_set.all()[:8]
            data = serializers.serialize("json", answers)
        else:
            answers = question.answer_set.filter(title__icontains=search)[:8] 
            data = serializers.serialize("json", answers)
    except Question.DoesNotExist:
            raise Http404
    
    return HttpResponse(data, content_type='application/json')

#Custom 404 error page
def error_404_view(request, exception):
    return HttpResponse("Page Not Found")