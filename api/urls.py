from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'api'

urlpatterns = [
	path('token/', obtain_auth_token, name='obtain_auth_token'),

	path('get-all-series/', views.getAllSeries, name='get_all_series'),
	path('get-all-serie-questions/<str:pk>/', views.getOneSerieQuestions, name='get_all_serie_questions'),

	path('export-series/', views.seriesExport, name='export_series'),
	path('export-questions/', views.questionsExport, name='export_questions'),
	path('export-answers/', views.answersExport, name='export_answers'),

	path('get-automation-data2/', views.getAutomationData2, name='get_data2'),
	path('myautomation-data/', views.myAutomationData, name='get_data'),
	path('get-automation-data3/', views.getAutomationData3, name='get_data3'),
	path('get-automation-data-commentrep/', views.getAutomationDataCommentRep, name='get_data4'),
	path('get-automation-data-postrep/', views.getAutomationDataDownVote, name='get_data5'),
	
	# path('series-list/', views.SeriesList.as_view(), name='series_list'),
	# path('series-detail/<uuid:pk>/', views.SerieDetail.as_view(), name='serie_detail'),
	# path('questions-list/', views.QuestionsList.as_view(), name='questions_list'),
	# path('question-detail/<uuid:pk>/', views.QuestionDetail.as_view(), name='question_detail'),
	

]