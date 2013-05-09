# Create your views here.
from django.shortcuts import render
from map.models import Boat
import xml.etree.ElementTree as ET
import urllib2

class TBoat:
    def __init__(self, name=None):
        if name is None:
            self.name=''
            self.popup=''
        else:
            try:
                b = Boat.objects.get(tpname=name)
                self.name = b.name
                self.popup="<b>%s</b><br/><img src='%s'/>" % (b.name,b.image)
            except Boat.DoesNotExist:
                self.name = name
                self.popup='no record'
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
        b = TBoat()
        b.name = name
        b.lat = loc['lat']
        b.lng = loc['lng']
        boats.append(b)
    return boats

def index(request):
    local_db = Boat.objects.all()
    context = {'local_db': local_db, 'trackaphone': trackaphone()}
    return render(request, 'map/index.html', context)
