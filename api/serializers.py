from rest_framework import serializers
from . import models




class SerieSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Serie
		fields = ('id', 'title',)


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Answer
		fields = ('answer', 'is_right',)


class QuestionSerializer(serializers.ModelSerializer):
	all_answers = AnswerSerializer(read_only=True, many=True)
	class Meta:
		model = models.Question
		fields = ('title', 'image', 'all_answers')