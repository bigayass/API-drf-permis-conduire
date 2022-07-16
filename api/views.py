from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_csv.renderers import CSVRenderer
from . import models, serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAutomationData2(request):
	# data = {
	# 	"link": "https://9gag.com/",
	# 	"profiles_url": "/Users/a123456/Library/Application Support/Google/Chrome",
	# 	"chrome_driver": "chromedriver",
	# 	"search_btn": "//*[@id='top-nav']/div/div/div[1]/a",
	# 	"search_input": "//*[@id='top-nav']/div/div/div[1]/div/div/form/div/input",
	# 	"tags_buttons": "ui-search-item",
	# 	"feresh_tag": '//*[@id="page"]/div[2]/div[1]/div/ul/li[2]/a',
	# 	"up_buttons": "up",
	#	"elemnts_number": 0
	# }
	#/Users/a123456/Library/Application Support/Google/Chrome
	#C:\\Users\\Yasse\\AppData\\Local\\Google\\Chrome\\User Data
	data = {
		"1": "https://9gag.com/",
		"2": "/Users/a123456/Library/Application Support/Google/Chrome",
		"3": "chromedriver",
		"4": "//*[@id='top-nav']/div/div/div[1]/a",
		"5": "//*[@id='top-nav']/div/div/div[1]/div/div/form/div/input",
		"6": "ui-search-item",
		"7": '//*[@id="page"]/div[2]/div[1]/div/ul/li[2]/a',
		"8": "up",
		"9": 0
	}

	return Response(data, status=status.HTTP_200_OK)


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



class SeriesRenderer(CSVRenderer):
    header = ['Id', 'Title']

class QuestionRenderer(CSVRenderer):
    header = ['Serie_id', 'Title', 'Image']

class AnswerRenderer(CSVRenderer):
    header = ['Quesion_id', 'Answer', 'Is_right']


@api_view(['GET'])
@renderer_classes([SeriesRenderer])
def seriesExport(request):
    series = models.Serie.objects.all().order_by('date_created')
    content = [{'Id': serie.id,
    			'Title': serie.title }
               for serie in series]

    return Response(content, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([QuestionRenderer])
def questionsExport(request):
    questions = models.Question.objects.all().order_by('date_created')
    content = [{'Serie_id': qs.serie.id,
    			'Title': qs.title,
    			'Image': qs.image.url }
               for qs in questions]

    return Response(content, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([AnswerRenderer])
def answersExport(request):
    answers = models.Answer.objects.all()
    content = [{'Quesion_id': answer.question.id,
    			'Answer': answer.answer,
    			'Is_right': answer.is_right }
               for answer in answers]

    return Response(content, status=status.HTTP_200_OK)

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