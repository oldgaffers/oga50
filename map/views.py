# Create your views here.
from django.shortcuts import render
from map.models import Boat


def index(request):
    latest_map = Boat.objects.all()
    context = {'latest_map': latest_map}
    return render(request, 'map/index.html', context)
