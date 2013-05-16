#!/app/.heroku/python/bin/python

from map.models import Boat
from string import capwords
import xml.etree.ElementTree as ET
import urllib2
from dateutil import parser

def updateBoat(row, pin):
        mmsi = row.get('MMSI','')
        name = capwords(row.get('SHIPNAME',''))
        tpname = row.get('TPNAME','')
        timestamp = row.get('TIMESTAMP',datetime.utcnow().isoformat())
        lng = row['LON']
        lat = row['LAT']
        try:
            if mmsi != '':
                b = Boat.objects.get(mmsi=mmsi)
            elif tpname != '':
                b = Boat.objects.get(tpname=tpname)
            else:
                b = Boat.objects.get(name=name)
            if b.last_fix != '':
                last_fix = datetime.datetime(2013,4,1)
            else:
                last_fix = parser.parse(b.lastfix)
            new_fix = parser.parse(timestamp)
            if last_fix < new_fix:
                b.lng = lng
                b.lat = lat
                if b.pin != 'tkIcon':
                    b.pin = pin
                b.save()
        except Boat.DoesNotExist:
            b = Boat.objects.create(name=name, tpname=tpname, mmsi=mmsi, lat=lat, lng=lng, last_fix=timestamp, pin=pin)
            b.save()

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

#<?xml version="1.0" encoding="UTF-8"?><publisher><map-params enable-map-type="true" enable-overview="false" enable-pan="true" enable-scale="true"/><devices history-opacity="0.8" history-thickness="4"><device history-colour="#EC5252" icon-anchor-x="-1" icon-anchor-y="-1" icon-height="-1" icon-url="" icon-width="-1" label-content="Barrys Boat Lake District" name="Barrys Boat Lake District"><loc lat="54.235521" lng="-2.726719" time="Wed 15/05/13 17:05:47"/></device></devices></publisher>
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
        data['TIMESTAMP'] = parser.parse(loc['time']).isoformat()
        updateBoat(data, 'tpIcon')

