import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'oga50.settings'

from map.refresh import trackaphone,mt
trackaphone()
mt()
