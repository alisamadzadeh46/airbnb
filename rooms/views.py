from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models
from django.views.generic import ListView


class HomeView(ListView):
    model = models.Room
