from django.contrib import admin
from .models import *


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
