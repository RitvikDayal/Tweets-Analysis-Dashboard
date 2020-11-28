import os
import random
import pandas as pd
from django.conf import settings
from collections import Counter

# Rest Frame Work Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# Constant/Global variables
base = settings.BASE_DIR
df_tweets = pd.read_csv(os.path.join(base, 'analyzed_data.csv'))
covid_cases = pd.read_csv(os.path.join(base, 'covid_cases.csv'))


# Supportive Functions
def separateWords(data):
    words = []
    for line in data:
        if type(line) != type(10.0):
            for word in line.split():
                words.append(word)
    return words

def countWords(data):
    freq = Counter(data).most_common(15)
    freq = pd.DataFrame(freq)
    freq.columns = ['word', 'frequency']
    return freq

# <----------------APIs------------------>

#Summary Endpoint
class SummaryReport(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        temp = df_tweets['Sentiment'].value_counts().reset_index()
        temp_stats = covid_cases

        data = {
            'Y':temp['index'],
            'X':temp['Sentiment'],
            'covid_stats':{
                'values': [
                    int(temp_stats['Deaths'].sum()),
                    int(temp_stats['Recovered'].sum()),
                    int(temp_stats['Confirmed'].sum()),
                  ],
                  'labels':['Deaths','Recovered','Confirmed']
            }
        }

        return Response(data)

# Datewise Covid Cases
class DateWiseCases(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        temp = covid_cases.groupby('Date').sum()
        temp.reset_index(inplace=True)

        data = {
            'Dates':temp['Date'],
            'Confirmed':temp['Confirmed'],
            'Recovered':temp['Recovered'],
            'Deaths':temp['Deaths'],
        }

        return Response(data)

# Date Wise Tweets
class DateWiseTweets(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        temp = df_tweets
        temp['Date'] = pd.to_datetime(temp['Date'])
        temp = temp['Date'].value_counts().reset_index()
        temp.sort_values(by='index', inplace=True)
        
        data = {
            'X':temp['index'],
            'Y':temp['Date'],
        }

        return Response(data)

# All type of Word Count

class wordCount(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        temp = df_tweets[['clean_text', 'Sentiment']]
        pos_temp = temp[temp['Sentiment'] == 'Positive']
        neg_temp = temp[temp['Sentiment'] == 'Negative']
        neu_temp = temp[temp['Sentiment'] == 'Neutral']

        words_freq = countWords(separateWords(list(temp['clean_text'])))
        pos_freq = countWords(separateWords(list(pos_temp['clean_text'])))
        neg_freq = countWords(separateWords(list(neg_temp['clean_text'])))
        neu_freq = countWords(separateWords(list(neu_temp['clean_text'])))        

        data = {
            'allwords': {
                'words': words_freq['word'],
                'freq': words_freq['frequency']
            },
            'poswords': {
                'words': pos_freq['word'],
                'freq': pos_freq['frequency']
            },
            'negwords':{
                'words': neg_freq['word'],
                'freq': neg_freq['frequency']
            },
            'neuwords':{
                'words': neu_freq['word'],
                'freq': neu_freq['frequency']
            }
        }

        return Response(data)


# Country Wise Covid Stats

class CovidTopStats(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        temp = covid_cases.groupby('Country/Region').sum()
        temp.reset_index(inplace=True)

        top_confirmed_cases = temp.sort_values(by='Confirmed', ascending=False)
        top_recovered_Cases = temp.sort_values(by='Recovered', ascending=False)
        top_deaths_cases = temp.sort_values(by='Deaths', ascending=False)

        data = {
            'topCases':{
                'Countries': top_confirmed_cases['Country/Region'][:6],
                'value':top_confirmed_cases['Confirmed'][:6],
            },
            'topRecovered':{
                'Countries': top_recovered_Cases['Country/Region'][:6],
                'value':top_recovered_Cases['Recovered'][:6],
            },
            'topDeaths':{
                'Countries': top_deaths_cases['Country/Region'][:6],
                'value':top_deaths_cases['Deaths'][:6],
            },
        }

        return Response(data)