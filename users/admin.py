from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'is_active', 'language', 'currency', 'superhost', 'is_staff',
        'is_superuser')
    list_filter = UserAdmin.list_filter + (
        "superhost",
    )
    search_fields = list_display
