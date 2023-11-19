from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BirdConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bird"
    verbose_name = _("Vögel")
