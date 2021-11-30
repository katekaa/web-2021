from django.shortcuts import render


from django.http import HttpResponse

stations = [
            {'title': 'Театральная', 'id': 0, 'line':'Замоскворецкая' , 'district': 'Тверской', 'year':'1938'},
            {'title': 'Бауманская', 'id': 1, 'line':'Арбатско-Покровская' , 'district': 'Басманный', 'year':'1944'},
            {'title': 'Ростокино', 'id': 2, 'line':'Московское Центральное Кольцо' , 'district': 'Ярославский', 'year':'2016'},
        ]

def getStations(request):
    return render(request, 'stations.html', { 'data' : {
        'stations': stations
    }})

def getStation(request, id):
    context =  {'id': id, 'station': stations[id]}
    return render(request, 'station.html', context)
