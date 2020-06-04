import json

from django.conf import settings
from django.http import HttpResponse
from django.views import View


# Create your views here.

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        response = 'Coming soon'
        response += '<div><a href="/news" target="_blank">News</a>'
        return HttpResponse(response)


class NewsView(View):
    def get(self, request, *args, **kwargs):
        response = 'Coming soon'
        return HttpResponse(response)


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
                response += '<div><a href="/news/" target="_blank">News</a>'
        return HttpResponse(response)
