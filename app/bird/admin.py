from django.contrib import admin

from .models import Bird, FallenBird


@admin.register(FallenBird)
class FallenBirdAdmin(admin.ModelAdmin):
    list_display = [
        "bird",
        "age",
        "sex",
        "date_found",
        "place_found",
        "created",
        "updated",
        "user",
    ]
    list_filter = ("bird", "created", "user")


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ["name"]
