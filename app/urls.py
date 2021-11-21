from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('questions', views.questions, name="questions"),
    path('submit', views.submit, name='submit'),
    path('next',views.next, name='next'),
    path('previous',views.previous, name='previous'),
    path('finish',views.finish, name='finish'),
    path('CreateAccount',views.CreateAccount, name='CreateAccount'),
    path('accountCreation', views.accountCreation, name='accountCreation'),
    path('login',views.login, name='login'),
    path('addQuestions',views.addQuestions, name='addQuestions'),
    path('uploadQuestions', views.uploadQuestions, name='uploadQuestions'),
]