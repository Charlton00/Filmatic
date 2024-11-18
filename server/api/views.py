from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here
'''
def index(request):
    return HttpResponse("Hello World. You're at the api index!")
'''

class API(APIView):
    
    def get(self, request):
        song_titles = []
        for key in request.GET:
            #if key.startswith("song"):
            song_titles.append(request.GET[key])
        return JsonResponse({"songs": song_titles})