# quiz_game/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact),
    path('about/', views.about),
    path('guidelines/', views.guidelines),
    path('testimonial/', views.testimonial),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('quiz/', views.quiz, name='quiz'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
    path('video/', views.video, name='video'),
    path('score/', views.score, name='score'),
    path('save-score/', views.save_score, name='save_score'),
    path('view-feedbacks/', views.view_feedbacks, name='view_feedbacks'),
    path('view-scoreboard/', views.view_scoreboard, name='view_scoreboard'),
]