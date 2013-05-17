# Create your views here.
from django.shortcuts import render
from map.models import Boat

def index(request):
    local_db = Boat.objects.all()
    boats = []
    for b in local_db:
        b.popup = "<b>"+b.name+"</b>"
        if b.image.startswith('http:'):
            b.popup = b.popup + "</br><img width='100' height='100' src='"+b.image+"'/>"
        elif b.image != '':
            b.popup = "<b>"+b.name+"</b></br><img width='100' height='100' src='/map/static/map/"+b.image+"'/>"
        if b.blog!= '':
            b.popup = b.popup + "</br><a href='"+b.blog+"'>View log</a>"
        b.popup = b.popup + "</br>last fix: "+b.last_fix
        boats.append(b)
    context = {'boats': boats}
    return render(request, 'map/index.html', context)
