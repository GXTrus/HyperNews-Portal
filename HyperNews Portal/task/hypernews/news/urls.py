from django.urls import path
from news.views import CreatePostView, NewsView, PostView

from . import views

app_name = 'news'
urlpatterns = [
    path('create/', CreatePostView.as_view()),
    path('<int:post_id>/', PostView.as_view(), name='post_id'),
    path('', views.news_function, name = 'news'),
    ]
