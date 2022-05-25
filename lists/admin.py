from django.contrib import admin
from .models import *


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    pass
