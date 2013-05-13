# Create your views here.
from django.shortcuts import render
from map.models import Boat
import xml.etree.ElementTree as ET
import urllib2

def ais(boat):
    r = urllib2.urlopen("http://marinetraffic.com/ais/shipdetails.aspx?MMSI=" + boat.mmsi)
    html = r.read()
    p1 = html.find("&deg;")
    p2 = html.rfind(">", 0, p1) + 1
    p3 = html.find("&deg;", p1+1)
    p4 = html.rfind("/", p1, p3) + 1
    boat.lat = float(html[p2:p1])
    boat.lng = float(html[p4:p3])
    return boat

def index(request):
    local_db = Boat.objects.all()
    boats = []
    for b in local_db:
        b.popup=''
        if b.image != '':
            b.popup = "<b>"+b.name+"</b></br><img width='100' height='100' src='/map/static/map/"+b.image+"'/>"
        if b.blog!= '':
            b.popup = b.popup + "</br><a href='"+b.blog+"'>View log</a>"
        boats.append(b)
    #context = {'ais': boats, 'trackaphone': trackaphone()}
    context = {'boats': boats}
    return render(request, 'map/index.html', context)
