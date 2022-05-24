from django.contrib import admin
from .models import *


@admin.register(RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
