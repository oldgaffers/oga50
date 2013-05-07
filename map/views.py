# Create your views here.
from django.http import render

def index(request):
   latest_map = Boat.objects.all().order_by('-pub_date')[:5]
    context = {'latest_map': latest_map}
    return render(request, 'map/index.html', context)
