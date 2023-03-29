from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = HttpResponse()
    response.write("<p>Rango says he there Partner</p>")
    response.write("<a href = 'http://thejacksinclair.pythonanywhere.com/about'>Rango says he there Partner</a>")
    return response

def about(request):
    response = HttpResponse()
    response.write("<p>Rango says this is shite</p>")
    response.write("<a href = 'http://thejacksinclair.pythonanywhere.com/'>Rango says this is shite</a>")
    return response