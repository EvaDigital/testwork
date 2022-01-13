from django.contrib import admin
from .models import *


@admin.register(CreateSurvey)
class CreateSurveyAdmin(admin.ModelAdmin):
    list_display = ['survey_name']


@admin.register(CreateSurveyQuestion)
class CreateSurveyQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(ChoiceAnswer)
class ChoiceAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass