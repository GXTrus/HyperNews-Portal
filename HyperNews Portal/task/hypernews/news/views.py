import datetime
import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        response = 'Coming soon'
        response += '<h2>Hyper news</h2>'
        response += '<div><a href="/news/">News</a>'
        return HttpResponse(response)


class NewsView(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        for post_ in news:
            post_['date'] = post_['created'].split()[0]
        return render(request, 'news/news.html', context={'news': news, })


class News2View(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        for post_ in news:
            post_['datetime'] = datetime.datetime.strptime(post_['created'], "%Y-%m-%d %H:%M:%S")
        return render(request, 'news/news2.html', context={'news': news, })


class PostView(View):
    def get(self, request, post, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        response = ''
        for post_ in news:
            if str(post_['link']) == post:
                response = f'<h2>{post_["title"]}</h2>\n'
                response += f'<p>{post_["created"]}</p>\n'
                response += f'<p>{post_["text"]}</p>\n'
                response += '<div><a href="/news/">News</a></div>'
        return HttpResponse(response)
