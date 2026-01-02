# accounts/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("display_name", "profile_image", "dob")
    readonly_fields = ()

    def profile_image(self, obj):
        if obj.profile_pic:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:50%;" />',
                obj.profile_pic.url
            )
        return "—"

    profile_image.short_description = "Profile Pic"

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
