from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def getLines(request):
    return render(request, 'lines.html', { 'data' : {
        'lines': Lines.objects.all()
    }})

def getStation(request, id):
    return render(request, 'station.html', { 'data' : {
        'id': id,
        'stations': Stations.objects.filter(line=id)
    }})

# Create your views here.
