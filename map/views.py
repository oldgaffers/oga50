# Create your views here.
from django.shortcuts import render
from map.models import Boat

def popup(b):
    s = "<b>"+b.name+"</b>"
    if b.image != '':
        s += "<br/><img width='100' height='100' src='"+b.image+"'/>"
    if b.blog != '':
        s += "<br/><a href='"+b.blog+"'>View log</a>"
    if b.text != '':
        s += "<br/>"+b.text
    s += "</br>last fix: "+b.last_fix
    return s
    
def index(request):
    local_db = Boat.objects.all()
    boats = []
    for b in local_db:
        b.popup = popup(b)
        boats.append(b)
    context = {'boats': boats}
    return render(request, 'map/index.html', context)
