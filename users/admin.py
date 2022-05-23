from django.contrib import admin
from .models import *


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    list_filter = ("language", "currency", "superhost")
