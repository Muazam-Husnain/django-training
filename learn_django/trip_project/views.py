from django.shortcuts import render
from .models import Trip

def index(request):
    trips = Trip.objects.all()
    # print(trips)

    return render(request, 'triplist.html', {'trips': trips})


