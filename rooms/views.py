from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = models.Room

