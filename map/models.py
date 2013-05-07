from django.db import models

# Create your models here.
class Boat(models.Model):
    name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.name

