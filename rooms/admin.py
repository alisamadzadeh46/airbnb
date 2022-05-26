from django.contrib import admin
from .models import *


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")}
        ),

        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Space", {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules")
            }),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("host",)}),
    )
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
        "count_amenities",
        "count_photos",
        "total_rating",
        "instant_book")
    list_filter = (
        "host__superhost", "city", "country", "instant_book", "room_type", "amenities", "facilities", "house_rules")
    search_fields = ("=city", "^host__username")
    search_help_text = "search city and host"
    list_per_page = 5
    filter_horizontal = ("amenities", "facilities", "house_rules")
    ordering = ("name", "price", "bedrooms")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
