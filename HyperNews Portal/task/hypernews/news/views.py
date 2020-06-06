import datetime
import json
import random
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


# Create your views here.
def get_random(used):
    a = random.randint(1, 999999)
    if a in used:
        a = get_random(used)
    return a

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
                response += f'<h2>{post_["title"]}</h2>\n'
                response += f'<p>{post_["created"]}</p>\n'
                response += f'<p>{post_["text"]}</p>\n'
                response += '<div><a href="/news/">News</a></div>'
        return HttpResponse(response)


class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        # response = '<form method="post">{% csrf_token %}'
        # response += '<p>Title:</p>'
        # response += '<input type="text" name="title">'
        # response += '<p>Text:</p>'
        # response += '<input type="text" name="text">'
        # response += '<p><button type="submit">Submit</button></p>'
        # response += '</form>'
        # return HttpResponse(response)
        return render(request, 'news/create.html')

    def post(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_news:
            news = json.load(json_news)
        used_links = []
        for post in news:
            used_links.append(post['link'])
        link = get_random(used_links)
        title = request.POST.get('title')
        text = request.POST.get('text')
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_post_dict = { 'created': time, "text": text, "title": title, 'link': link}
        news.append(new_post_dict)
        with open("news.json", "w") as json_file:
            json.dump(news, json_file)
        # return HttpResponse(response)

        # return HttpResponse(line_of_cars.processing())
        return redirect('/news')
