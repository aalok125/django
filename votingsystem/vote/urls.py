from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('category/<str:category_slug>',views.CategoryView.as_view(), name="category"),
    path('poll/<str:question_slug>',views.PollPageView.as_view(), name="poll"),
    path('result/<str:question_slug>',views.PollResultView.as_view(), name="result"),
    path('poll/<str:question_slug>/filter_options',views.filter_options, name="filter_options"),
    path('poll/<str:question_slug>/<str:answer_pk>',views.VoteSelectView.as_view(), name="vote_selection"),
    
]

handler404 = 'vote.views.error_404_view'