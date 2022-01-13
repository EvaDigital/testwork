from asyncore import read
from dataclasses import field, fields
from email.policy import default
from pickletools import read_floatnl
from rest_framework import serializers
from .models import *


class CurrentUserDefault(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id


class AnswerSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=CurrentUserDefault)
    survey = serializers.SlugRelatedField(queryset=CreateSurvey.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=CreateSurveyQuestion.objects.all(), slug_field='id')
    choice_answer = serializers.SlugRelatedField(queryset=ChoiceAnswer.objects.all(), slug_field='id', allow_null=True)
    answer_text = serializers.CharField(max_length=255, allow_null=True, required=False)

    class Meta:

        model = Answer

        fields = (
            'user_id',
            'survey',
            'question',
            'choice_answer',
            'answer_text',
        )

        read_only_fields = ('id', )

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        question_type = CreateSurveyQuestion.objects.get(id=attrs['question'].id).question_type

        try:
            if str(question_type) == 'TEXT':
                obj = CreateSurveyQuestion.objects.get(uestion=attrs['question'].id, survey=attrs['survey'], 
                                                        user_id=attrs['user_id'])

            elif str(question_type) == 'CHOICE':
                obj = CreateSurveyQuestion.objects.get(uestion=attrs['question'].id, survey=attrs['survey'], 
                                                        user_id=attrs['user_id'])

            elif str(question_type) == 'MULTICHOICE':
                obj = Answer.objects.get(question=attrs['question'].id, survey=attrs['survey'],
                                         user_id=attrs['user_id'],
                                         choice=attrs['choice'])

        except Answer.DoesNotExist:
            return attrs
 

class ChoiceAnswerSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=CreateSurveyQuestion.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=255)

    class Meta:

        model = ChoiceAnswer

        fields = (
            'question',
            'choice_text',
        )

    def create(self, validated_data):
        return ChoiceAnswer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        try:
            obj = ChoiceAnswer.objects.get(question=attrs['question'].id, choice_text=attrs['choice_text'])
        except ChoiceAnswer.DoesNotExist:
            return attrs


class CreateSurveyQuestionSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    survey = serializers.SlugRelatedField(queryset=CreateSurvey.objects.all(), slug_field='id')
    question_text = serializers.CharField(max_length=200)
    question_type = serializers.CharField(max_length=200)
    choices = ChoiceAnswerSerializer(many=True, read_only=True)

    class Meta:

        model = CreateSurveyQuestion

        fields = (
            'id',
            'survey',
            'question_text',
            'question_type',
            'choices',
        )

        read_only_fields = ('id', )

    def create(self, validated_data):
        return CreateSurveyQuestion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def validate(self, attrs):
        question_type = attrs['question_type']

        if str(question_type) == 'TEXT':
                return attrs
        elif str(question_type) == 'CHOICE':
                return attrs

        elif str(question_type) == 'MULTICHOICE':
                return attrs
        else:
            raise serializers.ValidationError("Выберите один из типов вопроса")


class CreateSurveySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    survey_name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    pupublication_date = serializers.DateTimeField(read_only=True)
    end_date = serializers.DateTimeField()
    questions = CreateSurveyQuestionSerializer(many=True, read_only=True)

    class Meta:

        model = CreateSurvey

        fields = (
            'id',
            'survey_name',
            'description',
            'publication_date',
            'end_date',
            'questions',
        )

        read_only_fields = (
            'id', 
            'publication_date', 
        )

    def create(self, validated_data):
        return CreateSurvey.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
