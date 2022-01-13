from django.urls import path
from .views import *

urlpatterns =[
    path('login/', login, name='login'),
    # Опросы (surveys)
    path('surveys/create/', survey_create, name='survey_create'),
    path('survey/update/<int:survey_id>/', survey_update, name='survey_update'),
    path('surveys/view/', survey_view, name='survey_view'),
    path('surveys/view/active/', active_survey_view, name='active_survey_view'),
    # Вопрос (question)
    path('question/create/', question_create, name='question_create'),
    path('question/update/<int:question_id>/', question_update, name='question_update'),
    # Выбор (choice)
    path('choice/create/', choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', choice_update, name='choice_update'),
    # Ответ (answer)
    path('answer/create/', answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', answer_update, name='answer_update')
]