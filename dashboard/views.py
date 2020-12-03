import random
from django.shortcuts import render, redirect
from django.contrib import messages
from .api import df_tweets, covid_cases, getSentiment
import pandas as pd
from .forms import TweetInput

def home(request):
    return render(request, 'dashboard/home.html')

def dataCollection(request):
    return render(request, 'dashboard/data_collection.html')

def dashboard(request):
    fav = df_tweets.sort_values(by='favorite_count', ignore_index=True)
    ret = df_tweets.sort_values(by='retweet_count', ignore_index=True)
    temp = df_tweets['Sentiment'].value_counts().reset_index()

    context = {
        'StartDate': '2020-09-15 00:00:05',
        'EndDate': '2020-09-30 23:59:54',
        'TotalTweets': len(df_tweets),
        'TotalCases':len(covid_cases),
        'Neutral': temp['Sentiment'][0],
        'Positive': temp['Sentiment'][1],
        'Negative': temp['Sentiment'][2],
        'fav_tweets': fav['full_text'][:5],
        'ret_tweets': ret['full_text'][:5],
    }

    return render(request, 'dashboard/dashboard.html', context=context)

def insideTweets(request):
    context = {
        'Ids': random.sample(list(df_tweets['id']), 5),
    }
    return render(request, 'dashboard/inside_tweets.html', context=context)

def tweetsScrapper(request):
    return render(request, 'dashboard/tweets_scrapper.html')

def dataProcessing(request):
    return render(request, 'dashboard/data_preprocessing.html')

def analysis(request):
    return render(request, 'dashboard/the_analysis.html')


def realAnalyzer(request):
    if request.method == 'POST':
        form = TweetInput(request.POST)
        if form.is_valid():
            sentiment = getSentiment(form.data['tweet'])
            if sentiment == 'Positive Sentiment':
                messages.success(request, f'Tweet with {sentiment}!')
            elif sentiment == 'Negative Sentiment':
                messages.warning(request, f'Tweet with {sentiment}!')
            else:
                messages.info(request, f'Tweet with {sentiment}!')
            return redirect('analyzer')
        else:
            messages.warning(request, f'Tweets not submitted.')
    else:
        form = TweetInput()
    return render(request, 'dashboard/analyzer.html', {'form': form})