from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
# def index(request):
#     return HttpResponse("hello")

class HomeView(View):
    def get(self, request):
        context = {}
        return render(request,"front/index.html")


class CategoryView(View):
    def get(self, request):
        context = {}
        return render(request,"front/category.html")


class VotingPageView(View):
    def get(self, request):
        context = {}
        return render(request,"front/votingPage.html")


class VotingResultView(View):
    def get(self, request):
        context = {}
        return render(request,"front/votingResult.html")