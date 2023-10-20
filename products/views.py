from django.shortcuts import render
from django.http import HttpResponse
import datetime

def firstView(request):
    return HttpResponse("<h1>Welcome to GEEK SHOP<h1>")

def datetimeView(request):
    return HttpResponse(datetime.datetime.now())

def goodbyeView(request):
    return HttpResponse("<h1>Goodbye! See you again!<h1>")