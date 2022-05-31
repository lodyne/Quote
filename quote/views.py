from multiprocessing import context
from django_tables2 import SingleTableView
import requests
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView

from quote.models import Quote
from quote.tables import MyTable


# Create your views here.
def home(request):
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
        "X-RapidAPI-Key": "b799b564e4mshe9022c63f6e7e49p12a6bbjsndfd08f1175da"
    }

    response = requests.request("GET", url, headers=headers)
    # response = requests.get(url, headers=headers)

    data = response.json()

    context = {
        'content':data['content'],
        'originator':data['originator']['name']

    }
    
    return render(request,'quote/home.html',context)
    # return render(request,'quote/home.html',{'data':data})

class IndexView(TemplateView):
    queryset = Quote.objects.all()
    template_name = 'quote/index.html'

def index(request):
    data = Quote.objects.all()
    # context = {
    #     'data':data
    # }
    # return render(request,'quote/index.html',context)
    return render(request,'quote/index.html',{'data':data})

def another(request):
    data = {
        'name':'lodger',
        'age' : 28,
        'career': 'developer'
    }
    return render(request,'quote/another.html',{'data': data})
    
    
def another1(request):
    data = {
        'name':'lodger mtui',
        'age' : 28,
        'career': 'software developer'
    }

    return render(request,'quote/another1.html',data)

class TableView(SingleTableView):
    model = Quote
    table_class = MyTable
    template_name = 'quote/table.html'
