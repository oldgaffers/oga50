from django.db import models

# Create your models here.
class Boat(models.Model):
    name = models.CharField(max_length=70)
    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return self.name

class Boat2(models.Model):
    name = models.CharField(max_length=70)
    image = models.CharField(max_length=200)
    blog = models.CharField(max_length=200)
    tpname = models.CharField(max_length=70)
    mmsi = models.CharField(max_length=20)
    home_port = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    text = models.CharField(max_length=400)
    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return self.name

