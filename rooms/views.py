from django.http import HttpResponse
from django.shortcuts import render


def all_rooms(request):
    return HttpResponse(content="Hi")
