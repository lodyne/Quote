import requests
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
        "X-RapidAPI-Key": "b799b564e4mshe9022c63f6e7e49p12a6bbjsndfd08f1175da"
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    context = {
        'content':data['content'],
        'originator':data['originator']['name']

    }
    
    # return render(request,'quote/index.html',context)
    return render(request,'quote/home.html',context)

# class IndexView(TemplateView):
#     template_name = 'quote/index.html'
    

