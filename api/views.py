from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from . import models, serializers


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getAllSeries(request):
	series = models.Serie.objects.filter(is_active=True)
	serializer = serializers.SerieSerializer(series, many=True)

	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getOneSerieQuestions(request, pk):
	serie = get_object_or_404(models.Serie, id=pk)
	questions = serie.questions.all()
	serializer = serializers.QuestionSerializer(questions, many=True)

	return Response(serializer.data, status=status.HTTP_200_OK)



"""
class SeriesList(generics.ListCreateAPIView):
	permission_classes = [AllowAny]
	queryset = models.Serie.objects.all()
	serializer_class = serializers.SerieSerializer


class SerieDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [AllowAny]
	queryset = models.Serie.objects.all()
	serializer_class = serializers.SerieSerializer


class QuestionsList(generics.ListCreateAPIView):
	permission_classes = [AllowAny]
	queryset = models.Question.objects.all()
	serializer_class = serializers.QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [AllowAny]
	queryset = models.Question.objects.all()
	serializer_class = serializers.QuestionSerializer
"""