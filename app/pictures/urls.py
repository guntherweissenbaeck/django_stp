from django.urls import path

from .views import (
    pictures_all,
    pictures_single,
    #  pictures_edit,
    pictures_delete,
)

urlpatterns = [
    path("all/", pictures_all, name="pictures_all"),
    path("single/<id>", pictures_single, name="pictures_single"),
    #  path("edit/<id>", pictures_edit, name="pictures_edit"),
    path("delete/<id>", pictures_delete, name="pictures_delete"),
]
