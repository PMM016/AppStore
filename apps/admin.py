from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "icon", "icon_url", "icon_font")
    search_fields = ("name",)


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)


@admin.register(SubFolder)
class SubFolderAdmin(admin.ModelAdmin):
    list_display = ("title", "folder", "description")
    list_filter = ("folder",)
    search_fields = ("title",)


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "icon_preview",
        "folder_list",
        "sub_folder",
        "status",

    )

    list_filter = (
        "status",
        "folders",
        "sub_folder",
    )

    search_fields = (
        "name",
        "categories",
        "use",
        "description",
    )

    filter_horizontal = ("folders", "categories",)
    
    prepopulated_fields = {"slug": ("name",)}

    ordering = ("name",)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html(
                '<img src="{}" style="width:32px;height:32px;object-fit:contain;" />',
                obj.icon.url
            )
        if obj.icon_url:
            return format_html(
                '<img src="{}" style="width:32px;height:32px;object-fit:contain;" />',
                obj.icon_url
            )
        return "—"

    icon_preview.short_description = "Icon"

    def folder_list(self, obj):
        return ", ".join(folder.title for folder in obj.folders.all())

    folder_list.short_description = "Folder(s)"

    def use_short(self, obj):
        return obj.use[:50] + "..." if len(obj.use) > 50 else obj.use

    use_short.short_description = "Use"
