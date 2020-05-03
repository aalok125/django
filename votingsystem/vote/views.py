from django.shortcuts import render, HttpResponse, Http404, redirect
from django.views import View
from .models import *
from django.utils.decorators import method_decorator
from random import randint
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from .filters import CategoryFilter
from .decorators import attempt_check
from .geo_ip import lon_lat

# Create your views here.
# def index(request):
#     return HttpResponse("hello")

class HomeView(View):
    template_name = "front/index.html"

    def get(self, request):
        val3 = request.session.get('last_activity')
        val1 = request.session.get('guest_user')
        val2 = request.session.get('guest_ip')
        # return HttpResponse(str(val1)+" "+str(val2)+ " "+str(val3))
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

def filter_category(request):
    search = request.GET.get('title')
    categories = Category.objects.filter(title__icontains=search)[:4] 
    for category in categories:
        category.image_url = category.image.url
        if category.parent:
            category.page_url = "/"+category.parent.slug+"/"+category.slug
        else:
            category.page_url = "/"+category.slug
    data = serializers.serialize("json", categories)
    return HttpResponse(data, content_type='application/json')


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

class CategoryQuestionView(View):
    template_name = "front/category_questions.html"

    def get(self, request, parent_cat, child_cat):
        try:
            category = Category.objects.get(slug=parent_cat)
            subCategory = Category.objects.get(parent = category.id, slug=child_cat)
            
            #paginator
            questions = subCategory.question_set.all()
            paginator = Paginator(questions,20)
            page = request.GET.get('page')
            questions = paginator.get_page(page)

            dictionary = {
                'category':category,
                'subCategory':subCategory,
                'questions':questions
            }
        except Category.DoesNotExist:
            raise Http404
        return render(request, self.template_name, context=dictionary)

class PollPageView(View):
    template_name = "front/votingPage.html"

    @method_decorator(attempt_check)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def log_question(self, question, guest_id, *args, **kwargs):
        guest = GuestUser.objects.get(pk=guest_id)
        longitude, latitiude = lon_lat(guest.ipaddress) #tuple of lat, lon
        log = GuestUserLog(question=question, guest_user=guest, latitude=latitiude, longitude=longitude)
        log.save()
        pass

    def get(self, request, question_slug):    
        try:
            question = Question.objects.get(slug=question_slug)
            self.log_question(question, request.session.get('guest_user'))
            dictionary = {
                'question':question
            }
        except Question.DoesNotExist:
            raise Http404
        return render(request,self.template_name, context=dictionary)

class VoteNowView(View):
    def post(self, request, ques_pk):
        if(request.POST):
            try:
                answer_id = request.POST.get('option')
                guest_user = GuestUser.objects.get(pk=request.session.get('guest_user'))
                answer = Answer.objects.get(pk=answer_id)
                uservote = UserVote(guest_user = guest_user, answer = answer, question = answer.question)
                uservote.save()
            except Answer.DoesNotExist:
                raise Http404("Answer Not Found")
            return HttpResponse('vote registered')
        else:
            raise Http404

class PollResultView(View):
    template_name = "front/votingResult.html"
    def sorted_answer_by_votes(self, answers,*args, **kwargs):
        for answer in answers:
            answer.votes = answer.uservote_set.all().count()
        sorted_answers = sorted(answers, key=lambda t: t.votes, reverse=True)
        return sorted_answers
    def get(self, request, question_slug):
        try:
            question = Question.objects.get(slug=question_slug)
            answers = self.sorted_answer_by_votes(question.answer_set.all())
            dictionary = {
                'answers':answers
            }
        except Question.DoesNotExist:
                raise Http404("Answer Not Found")
        return render(request,self.template_name, context=dictionary)

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