from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

# Create your views here.

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        response = 'Coming soon'
        return HttpResponse(response)
