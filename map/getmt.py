from map.models import Boat
from string import capwords
import xml.etree.ElementTree as ET
import urllib2

def updateBoat(row, pin):
        mmsi = row.get('MMSI','')
        name = capwords(row.get('SHIPNAME',''))
        lng = row['LON']
        lat = row['LAT']
        try:
            if name == '':
                b = Boat.objects.get(mmsi=mmsi)
            else:
                b = Boat.objects.get(name=name)
            b.lng = lng
            b.lat = lat
        except Boat.DoesNotExist:
            b = Boat.objects.create(name=name, mmsi=mmsi, lat=lat, lng=lng)
        b.pin = pin
        b.tpname = row.get('TPNAME','')
        b.save()
        print b.name

def mt_update(xml):
    root = ET.fromstring(xml)
    for n in root:
        updateBoat(n.attrib, 'mtIcon')

# <POS><row TIMESTAMP="2013-05-12T19:25:00" STATUS="99" COURSE="0" SPEED="0" LON="-5.065115" LAT="50.154209" MMSI="235014887"/></POS>
def mt():
    r = urllib2.urlopen("http://services.marinetraffic.com/api/exportvessels/f0458439888b8e2eec63b8e8ae02b170d45790c4/timespan:60")
    xml = r.read()
    mt_update(xml)

def mt_long():
    r = urllib2.urlopen("http://services.marinetraffic.com/api/exportvessels/f0458439888b8e2eec63b8e8ae02b170d45790c4/timespan:60/msgtype:extended")
    xml = r.read()
    mt_update(xml)

def trackaphone():
    r = urllib2.urlopen("http://trackaphone.co.uk/callback/publish?id=1366120222963T569D3PYVN9B")
    xml = r.read()
    root = ET.fromstring(xml)
    for n in root[1]:
	data = {}
        device = n.attrib
        loc = n[0].attrib
        tpname = device['name']
        data['SHIPNAME'] = capwords(tpname.split(' - ')[0])
        data['TPNAME'] = tpname
        data['LAT']  = loc['lat']
        data['LON'] = loc['lng']
        updateBoat(data, 'tpIcon')
