from django.urls import path
from django.shortcuts import HttpResponse
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('<str:category_slug>/',views.CategoryView.as_view(), name="category"),
    path('<str:parent_cat>/<str:child_cat>/polls/',views.CategoryQuestionView.as_view(),name="category_questions"),
    path('poll/<str:question_slug>',views.PollPageView.as_view(), name="poll"),
    path('poll/<str:question_slug>/filter_options',views.filter_options, name="filter_options"),  #url for ajax filter of options
    path('filter_category/',views.filter_category, name="filter_category"),  #url for ajax filter of options
    path('<int:ques_pk>/vote_now/',views.VoteNowView.as_view(),name="vote_now"),
    path('result/<str:question_slug>',views.PollResultView.as_view(), name="result"),
]

handler404 = 'vote.views.error_404_view'