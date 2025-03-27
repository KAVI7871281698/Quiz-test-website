from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index1'),
    path('register',views.regiester,name='register'),
    path('login',views.login,name='login'),
    path('loggout',views.loggout,name='loogout'),
    path('admin1',views.admin,name='admin1'),
    path('out',views.out,name='out'),
    path('per',views.per,name='per'),
    path('ques',views.ques,name='ques'),
    path('quiz',views.quiz,name='quiz'),
    path('result',views.result,name='result'),
    path('student',views.student,name='student'),
    path('eco',views.economics,name='eco'),
    path('science',views.sci,name='science'),
    path('arts',views.art,name='arts'),
    path('politics',views.politic,name='politics'),
    path('cluture',views.clutures,name='cluture'),
    path('history',views.his,name='history'),
    path('quiz_submission', views.quiz_submission, name='quiz_submission'),
    path('quiz_form',views.quiz_form,name='quiz_form'),
    # path('quiz_pages/<int:id>/', views.quiz_pages, name='quiz_pages'),
    # path('<int:id>/submit/', views.submit_quiz, name='submit_quiz'),
]