# Create your views here.
from django.shortcuts import render
from map.models import Boat
import xml.etree.ElementTree as ET
import urllib2

class TBoat:
    def __init__(self, name=None):
        if name is None:
            self.name=''
            self.image=''
        else:
            try:
                b = Boat.objects.get(tpname=name)
                self.name = b.name
                self.image = b.image
            except Boat.DoesNotExist:
                self.name = name
                self.image=''
        self.lat = 0.0
        self.lng = 0.0

def trackaphone():
    r = urllib2.urlopen("http://trackaphone.co.uk/callback/publish?id=1366120222963T569D3PYVN9B")
    xml = r.read()
    root = ET.fromstring(xml)
    boats = []
    for n in root[1]:
        device = n.attrib
        loc = n[0].attrib
        name = device['name']
        b = TBoat(name)
        b.lat = loc['lat']
        b.lng = loc['lng']
        boats.append(b)
    return boats

def ais(boat):
    r = urllib2.urlopen("http://marinetraffic.com/ais/shipdetails.aspx?MMSI=" + boat.mmsi)
    html = r.read()
    p1 = html.find("&deg;")
    p2 = html.rfind(">", 0, p1) + 1
    p3 = html.find("&deg;", p1+1)
    p4 = html.rfind(" ", p3) + 1
    boat.lat = html[p2:p1]
    boat.lng = html[p4:p3]
    return boat

def index(request):
    local_db = Boat.objects.exclude(mmsi='')
    boats = []
    for b in local_db:
        boats.append(ais(b))
    context = {'ais': boats, 'trackaphone': trackaphone()}
    return render(request, 'map/index.html', context)
