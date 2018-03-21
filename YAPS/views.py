from django.shortcuts import render
from django.http import HttpResponse
from YAPS.models import Podcast


def index(request):
   
    response = render(request, 'YAPS/index.html')

    return response

def podcast(request):

    context_dict = {}





    response = render(request, 'YAPS/podcast.html')

    return response
