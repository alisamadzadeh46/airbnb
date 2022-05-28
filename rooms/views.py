from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models
from django.views.generic import ListView


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request):
    render(request, "rooms/detail.html")
