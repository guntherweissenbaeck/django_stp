from django.contrib import admin
from django.urls import path, include
from bird import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Dynamic sites
    path("", views.bird_all, name="index"),
    path("bird/", include("bird.urls")),
    path("contacts/", include("contact.urls")),
    path("costs/", include("costs.urls")),
    path("export/", include("export.urls")),
    path("pictures/", include("pictures.urls")),
    # Admin
    path("admin/", admin.site.urls),
    # Allauth
    path("accounts/", include("allauth.urls")),
]

# how to add the path for the media files
MEDIA_URL = "/media/"
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
