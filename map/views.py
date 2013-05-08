# Create your views here.
from django.shortcuts import render
from map.models import Boat
import xml.etree.ElementTree as ET
import urllib2

def trackaphone():
    r = urllib2.urlopen("http://trackaphone.co.uk/callback/publish?id=1366120222963T569D3PYVN9B")
    xml = r.read()
    root = ET.fromstring(xml)
	boats = {}
    for n in root[1]:
        device = n.attrib
        loc = n[0].attrib
        name = device['name']
        boats['name'] = {'name': name, lat: loc['lat'], lng: loc['lng']}
    return boats

def index(request):
    latest_map = Boat.objects.all()
    context = {'latest_map': latest_map}
    return render(request, 'map/index.html', context)
