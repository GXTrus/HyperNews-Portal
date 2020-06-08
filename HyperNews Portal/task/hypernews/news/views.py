import datetime
import json
from . import forms

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
import requests



# Create your views here.

def TestView(request):
    # def get(self, request, *args, **kwargs):
    response = 'Coming soon'
    response += '<h2>Hyper news</h2>'
    response += '<div><a href="/news/">News</a>'
    # return redirect('/news')
    return HttpResponse(response)


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        response = 'Coming soon'
        response += '<h2>Hyper news</h2>'
        response += '<div><a href="/news/">News</a>'
        return redirect('/news')
        # return HttpResponse(response)


class LatestNewsView(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        ordered_news = news.sort('-created')
        return HttpResponse(ordered_news)


class NewsView(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        q = request.GET.get('q')

        if q:
            new_news = []
            for post_ in news:
                if q in post_['title']:
                    new_news.append(post_)
            news = new_news
        for post_ in news:
            post_['date'] = post_['created'].split()[0]
        return render(request, 'news/news.html', context={'news': news, 'form': forms.NewsForm})

    def post(self, request, *args, **kwargs):
        params = {'q': request.POST.get('q')}
        return redirect('/', params=params)
        # return HttpResponse(response)
        # return HttpResponse(line_of_cars.processing())
        # requests.get('news/', params=params)


def news_function(request):
    if request.method == "POST":
        params = {'q': request.POST.get('q')}
        redirect_uri = request.GET.get('redirect_uri', "/home/")
        if "redirect_uri" == request.path:
            # avoid loops
            redirect_uri = "/home/"
        return redirect(redirect_uri)
    if request.method == 'GET':
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        q = request.GET.get('q')

        q = request.GET.get('q')
        if q:
            new_news = []
            for post_ in news:
                if q in post_['title']:
                    new_news.append(post_)
            news = new_news
        for post_ in news:
            post_['date'] = post_['created'].split()[0]
        return render(request, 'news/news.html', context={'news': news})


class News2View(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        for post_ in news:
            post_['datetime'] = datetime.datetime.strptime(post_['created'], "%Y-%m-%d %H:%M:%S")
        return render(request, 'news/news2.html', context={'news': news, })


class PostView(View):
    def get(self, request, post_id, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        try:
            q = request.GET.get('q', '')
        except:
            q = 'No Q'
        response = f'{q} <br>'
        for a in news:
            if a['link'] == post_id:
                response += f'<h2>{a["title"]}</h2>\n'
                response += f'<p>{a["created"]}</p>\n'
                response += f'<p>{a["text"]}</p>\n'
        if response == '':
            response += '<H1>404 Nothing Found</H1>'
        response += '<div><a href="/news/">Main Page</a></div>'
        return HttpResponse(response)


class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create.html')

    def post(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        used_links = []
        for post in news:
            used_links.append(post['link'])
        link = max(used_links) + 1
        title = request.POST.get('title')
        text = request.POST.get('text')
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_post_dict = {'created': time, "text": text, "title": title, 'link': link}
        news.append(new_post_dict)
        with open("news.json", "w") as json_file:
            json.dump(news, json_file)
        # return HttpResponse(response)

        # return HttpResponse(line_of_cars.processing())
        return redirect('/news')
