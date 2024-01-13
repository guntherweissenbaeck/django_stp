from django.contrib import admin

from .models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ["fallenbird", "image", "date_uploaded"]
    # list_filter = ["fallenbird"]
