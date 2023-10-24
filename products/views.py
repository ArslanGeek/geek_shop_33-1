from django.shortcuts import render
from django.http import HttpResponse
from . import models
import datetime

def carListView(request):
    car_value = models.Car.objects.all()
    return render(request, 'car/car.html', {'car_key': car_value})

def firstView(request):
    return HttpResponse("<h1>Welcome to GEEK SHOP<h1>")

def datetimeView(request):
    return HttpResponse(datetime.datetime.now())

def goodbyeView(request):
    return HttpResponse("<h1>Goodbye! See you again!<h1>")