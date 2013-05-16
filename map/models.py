from django.db import models

# Create your models here.

class Boat(models.Model):
    name = models.CharField(max_length=70, blank=True)
    image = models.CharField(max_length=200, blank=True)
    blog = models.CharField(max_length=200, blank=True)
    tpname = models.CharField(max_length=70, blank=True)
    mmsi = models.CharField(max_length=20, blank=True)
    home_port = models.CharField(max_length=20, blank=True)
    link = models.CharField(max_length=200, blank=True)
    pin = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=400, blank=True)
    last_fix = models.CharField(max_length=25, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return self.name

