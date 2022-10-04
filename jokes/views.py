from django.http import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.


def index(request):
    url = 'https://catfact.ninja/fact'
    response = requests.get(url).json()
    fact = response['fact']
    return render(request, 'index.html', context={'text': fact})
