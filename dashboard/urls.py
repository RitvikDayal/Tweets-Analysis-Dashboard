from django.urls import path
from . import views
from .api import SummaryReport, DateWiseTweets, wordCount

urlpatterns = [
    # Webpage Routes
    path('', views.home, name='home'),
    path('data-collection/', views.dataCollection, name='datacollection'),
    path('analyzer/', views.realAnalyzer, name='analyzer'),
    path('overview/', views.dashboard, name='overview'),
    path('tweets/', views.insideTweets, name='inside_tweets'),
    path('scrapper/', views.tweetsScrapper, name='scrapper'),
    path('analysis/', views.analysis, name='analysis'),
    path('dataprocessing/', views.dataProcessing, name='cleaning'),
    
    # API ENDPOINTS
    path('api/data/summary/', SummaryReport.as_view(), name='summary'),
    path('api/data/dateWiseTweets/', DateWiseTweets.as_view(), name='dateWiseTweets'),
    path('api/data/wordCount/', wordCount.as_view(), name='wordCount'),
]