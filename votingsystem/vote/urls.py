from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view()),
    path('category/',views.CategoryView.as_view()),
    path('voting/',views.VotingPageView.as_view()),
    path('result/',views.VotingResultView.as_view()),
]