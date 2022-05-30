from django.contrib import admin
from .models import *


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "users",
        "count_rooms"
    )
    search_fields = ("name",)

    filter_horizontal = ("rooms",)
