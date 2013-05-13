from map.refresh import trackaphone,mt
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'oga50.settings'
trackaphone()
mt()
