from django.contrib import admin

from .models import Bird, FallenBird


@admin.register(FallenBird)
class FallenBirdAdmin(admin.ModelAdmin):
    list_display = [
        "bird",
        "bird_identifier",
        "age",
        "sex",
        "date_found",
        "place_found",
        "place_found_other",
        "created",
        "updated",
        "status_changed",
        "user",
    ]
    list_filter = ("bird", "created", "user")


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ["name"]
