from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .algorithm import Algorithm

# Create your views here
'''
def index(request):
    return HttpResponse("Hello World. You're at the api index!")
'''

class API(APIView):
    
    def get(self, request):
        song_titles = []
        for key in request.GET:
            song_titles.append(request.GET[key])
            print(request.GET[key])
        print(Algorithm.get_spotify_token())
        return JsonResponse({"songs": song_titles})