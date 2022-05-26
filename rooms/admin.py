from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

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

    raw_id_fields = ("host",)

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
    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
