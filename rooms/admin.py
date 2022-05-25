from django.contrib import admin
from .models import *


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
