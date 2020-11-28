from django.urls import path
from . import views
from .api import SummaryReport, DateWiseTweets, wordCount

urlpatterns = [
    # Webpage Routes
    path('', views.home, name='home'),
    path('tweets/', views.insideTweets, name='inside_tweets'),
    path('scrapper/', views.tweetsScrapper, name='scrapper'),
    
    # API ENDPOINTS
    path('api/data/summary/', SummaryReport.as_view(), name='summary'),
    path('api/data/dateWiseTweets/', DateWiseTweets.as_view(), name='dateWiseTweets'),
    path('api/data/wordCount/', wordCount.as_view(), name='wordCount'),
]