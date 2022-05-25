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
    list_filter = ("city", "country", "instant_book")
    search_fields = ("=city", "^host__username")
    search_help_text = "search city and host"
    list_per_page = 5


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
