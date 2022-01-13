from tabnanny import verbose
from django.db import models


class CreateSurvey(models.Model):
    '''
    Model: CreateSurvey

    Attributes:
        survey_name: survey name
        publication_date: survey start date
        end_date: survey end date
        description: survey description
    '''

    survey_name = models.CharField(max_length=255, verbose_name="Название опроса")
    description = models.CharField(max_length=255, verbose_name="Описание опроса", blank=True)
    publication_date = models.DateTimeField(verbose_name="Дата начала опроса", help_text="Формат даты: ГГГГ-ММ-ДД, Формат времени: ЧЧ:ММ")
    end_date = models.DateTimeField(verbose_name="Дата окончания опроса",  help_text="format: ГГГГ-ММ-ДД, Формат времени: ЧЧ:ММ")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опрос"

    def __str__(self):
        return self.survey_name


class CreateSurveyQuestion(models.Model):
    '''
    Model: CreateSurveyQuestion

    Attributes:
        survey: the survey to which these questions relate
        question_text: question text
        question_type: question type
    '''

    class Type:
        TEXT = 'TEXT'
        CHOICE = 'CHOICE'
        MULTICHOICE = 'MULTICHOICE'

        choices = (
            (TEXT, 'TEXT'),
            (CHOICE, 'CHOICE'),
            (MULTICHOICE, 'MULTICHOICE'),
        )

    survey = models.ForeignKey(CreateSurvey, related_name="questions", on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=11, choices=Type.choices, default=Type.TEXT)

    class Meta:
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question_text


class ChoiceAnswer(models.Model):
    
    question = models.ForeignKey(CreateSurveyQuestion, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Ответы для выбора"

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    '''
    Model: Answer

    Attributes:
        user_id: User ID of the responding user
        survey: survey name
        question: questions related to this survey
        answer_text: answer to question
    '''

    user_id = models.IntegerField()
    survey = models.ForeignKey(CreateSurvey, related_name='survey', on_delete=models.CASCADE)
    question = models.ForeignKey(CreateSurveyQuestion, related_name='question', on_delete=models.CASCADE)
    choice_answer = models.ForeignKey(ChoiceAnswer, related_name='choice', blank=True, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Ответы пользователей"

    def __str__(self):
        return f"User_id: {self.user_id}  Опрос: {self.survey}"  



