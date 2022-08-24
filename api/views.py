from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_csv.renderers import CSVRenderer
from . import models, serializers
from .utils import send_email_msg



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAutomationDataDownVote(request):
	# data = {
	# 	"profiles_url": "/Users/a123456/Library/Application Support/Google/Chrome",
	# 	"chrome_driver": "chromedriver",
	# 	"disable_blink": "AutomationControlled",
	# 	"down_class": 'down',
	# 	"other_btn": '//*[@id="jsid-post-a81g9bY"]/header/div/div[3]/div/a',
	# 	"report_1_btn": '//*[@id="jsid-post-a81g9bY"]/header/div/div[3]/div[2]/ul/li[6]/a',
	# 	"spam_btn": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div/div/div/div/div[1]',
	# 	"report_2_btn": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div[2]/button'
	# }
	send_email_msg("Down Vote and Report a Post")
	# data = {
	# 	"1": "/Users/a123456/Library/Application Support/Google/Chrome",
	# 	"2": "chromedriver",
	# 	"3": "AutomationControlled",
	# 	"4": 'down',
	# 	"5": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div/div/div/div/div[1]',
	# 	"6": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div[2]/button',
	# 	"7": -1
	# }
	data = {
		"1": "1",
		"2": "2",
		"3": "3",
		"4": "4",
		"5": "5",
		"6": "6",
		"7": '7'
	}

	return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAutomationDataCommentRep(request):
	# data = {
	# 	"profiles_url": "/Users/a123456/Library/Application Support/Google/Chrome",
	# 	"chrome_driver": "chromedriver",
	# 	"down_vote": '//*[@id="page"]/div[1]/section[2]/section/section[2]/section[1]/section/div[2]/div[2]/div/button[2]',
	# 	"comment_btn": '//*[@id="page"]/div[1]/section[2]/section/section[2]/section[1]/section/div[2]/div[2]/div[2]/button',
	# 	"report_1_btn": '//*[@id="page"]/div[1]/section[2]/section/section[2]/section[1]/section/div[2]/div[2]/div[2]/ul/li[3]/button',
	# 	"spam_btn": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div/div/div/div/div[1]',
	# 	"report_2_btn": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div[2]/button'
	# }
	send_email_msg("Down Vote and Report a Comment")
	# data = {
	# 	"1": "/Users/a123456/Library/Application Support/Google/Chrome",
	# 	"2": "chromedriver",
	# 	"3": '//*[@id="page"]/div[1]/section[2]/section/section[2]/section[1]/section/div[2]/div[2]/div/button[2]',
	# 	"4": '//*[@id="page"]/div[1]/section[2]/section/section[2]/section[1]/section/div[2]/div[2]/div[2]/button',
	# 	"5": '//*[@id="page"]/div[1]/section[2]/section/section[2]/section[1]/section/div[2]/div[2]/div[2]/ul/li[3]/button',
	# 	"6": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div/div/div/div/div[1]',
	# 	"7": '//*[@id="jsid-app"]/div/div[2]/div/div[2]/div[2]/button'
	# }
	data = {
		"1": "1",
		"2": "2",
		"3": "3",
		"4": "4",
		"5": "5",
		"6": "6",
		"7": '7'
	}


	return Response(data, status=status.HTTP_200_OK)



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
	# 	"feresh_tag": '//*[@id="page"]/div[1]/div[2]/div/ul/li[2]/a',
	# 	"up_buttons": "up",
	#	"elemnts_number": 0
	# }
	#/Users/a123456/Library/Application Support/Google/Chrome
	#C:\\Users\\Yasse\\AppData\\Local\\Google\\Chrome\\User Data
	send_email_msg("Up Vote Post with chrome Profiles")
	# data = {
	# 	"1": "https://9gag.com/",
	# 	"2": "/Users/a123456/Library/Application Support/Google/Chrome",
	# 	"3": "chromedriver",
	# 	"4": "//*[@id='top-nav']/div/div/div[1]/a",
	# 	"5": "//*[@id='top-nav']/div/div/div[1]/div/div/form/div/input",
	# 	"6": "ui-search-item",
	# 	"7": '//*[@id="page"]/div[1]/div[2]/div/ul/li[2]/a',
	# 	"8": "up",
	# 	"9": 0
	# }
	data = {
		"1": "1",
		"2": "2",
		"3": "3",
		"4": "4",
		"5": "5",
		"6": "6",
		"7": '7',
		"8": "8",
		"9": "9"
	}

	return Response(data, status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAutomationData3(request):
	# data = {
	# 	"link": "https://9gag.com/connect/google?next=%2F",
	# 	"csv_file": "emails.csv",
	# 	"split": ";",
	# 	"chrome_driver": "chromedriver",
	# 	"nav_prv": "--incognito",
	# 	"login_input": '//*[@id="identifierId"]',
	# 	"next_btn": '//*[@id="identifierNext"]/div/button',
	# 	"pass_input": '//*[@id="password"]/div[1]/div/div[1]/input',
	# 	"next_btn2":  '//*[@id="passwordNext"]/div/button',
	# 	"search_btn": "//*[@id='top-nav']/div/div/div[1]/a",
	# 	"search_input": "//*[@id='top-nav']/div/div/div[1]/div/div/form/div/input",
	# 	"tags_buttons": "ui-search-item",
	# 	"feresh_tag": '//*[@id="page"]/div[1]/div[2]/div/ul/li[2]/a',
	# 	"up_buttons": "up",
	# 	"elemnts_number": 0
	# }
	send_email_msg("Up Vote Post with gmail Auth")
	# data = {
	# 	"0": "https://9gag.com/connect/google?next=%2F",
	# 	"1": "emails.csv",
	# 	"2": ",",
	# 	"3": "chromedriver",
	# 	"4": "--incognito",
	# 	"5": '//*[@id="identifierId"]',
	# 	"6": '//*[@id="identifierNext"]/div/button',
	# 	"7": '//*[@id="password"]/div[1]/div/div[1]/input',
	# 	"8":  '//*[@id="passwordNext"]/div/button',
	# 	"9": "//*[@id='top-nav']/div/div/div[1]/a",
	# 	"10": "//*[@id='top-nav']/div/div/div[1]/div/div/form/div/input",
	# 	"11": "ui-search-item",
	# 	"12": '//*[@id="page"]/div[1]/div[2]/div/ul/li[2]/a',	   
	# 	"13": "up",
	# 	"14": 0
	# }

	data = {
		"1": "1",
		"2": "2",
		"3": "3",
		"4": "4",
		"5": "5",
		"6": "6",
		"7": '7',
		"8": "8",
		"9": "9",
		"10": "10",
		"11": "11",
		"12": "12",
		"13": "13",
		"14": "14"
	}

	return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myAutomationData(request):
	# data = {
	# 	"link": "https://9gag.com/",
	# 	"profiles_url": "/Users/a123456/Library/Application Support/Google/Chrome",
	# 	"chrome_driver": "chromedriver",
	# 	"search_btn": "//*[@id='top-nav']/div/div/div[1]/a",
	# 	"search_input": "//*[@id='top-nav']/div/div/div[1]/div/div/form/div/input",
	# 	"tags_buttons": "ui-search-item",
	# 	"feresh_tag": '//*[@id="page"]/div[1]/div[2]/div/ul/li[2]/a',
	# 	"up_buttons": "up",
	#	"elemnts_number": 0
	# }
	#/Users/a123456/Library/Application Support/Google/Chrome
	#C:\\Users\\Yasse\\AppData\\Local\\Google\\Chrome\\User Data
	send_email_msg("Up Vote Post with chrome Profiles")
	data = {
		"1": "https://9gag.com/",
		"2": "/Users/a123456/Library/Application Support/Google/Chrome",
		"3": "chromedriver",
		"4": "//*[@id='top-nav']/div/div/div[1]/a",
		"5": "//*[@id='top-nav']/div/div/div[1]/div/div/form/div/input",
		"6": "ui-search-item",
		"7": '//*[@id="page"]/div[1]/div[2]/div/ul/li[2]/a',
		"8": "up",
		"9": 0
	}
	# data = {
	# 	"1": "1",
	# 	"2": "2",
	# 	"3": "3",
	# 	"4": "4",
	# 	"5": "5",
	# 	"6": "6",
	# 	"7": '7',
	# 	"8": "8",
	# 	"9": "9"
	# }

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