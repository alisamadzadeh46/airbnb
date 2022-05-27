from django.http import HttpResponse
from django.shortcuts import render
from . import models


def all_rooms(request):
    rooms = models.Room.objects.all()
    data = {
        'rooms': rooms
    }
    return render(request, "rooms/home.html", data)
