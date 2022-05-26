from django.contrib import admin
from .models import *


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "room",
        "status",
        "check_in",
        "check_out"
    )
