from django.contrib import admin
from .models import *


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
