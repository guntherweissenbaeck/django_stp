from uuid import uuid4
from datetime import datetime
from django.db import models

from django.utils.translation import gettext_lazy as _


from bird.models import FallenBird

def upload_filename(instance, filename):
    ext = filename.split(".")[-1].lower()
    date = datetime.now().strftime("%Y/%m/%d")
    filename = f"{"media"}/{"pictures"}/{date}/{uuid4()}.{ext}"
    return filename

class Picture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name=_("ID"))
    fallenbird = models.ForeignKey(FallenBird, on_delete=models.CASCADE, verbose_name=_("Patient"))
    image = models.ImageField(upload_to=upload_filename, blank=True, null=True, verbose_name=_("Bild"))
    date_uploaded = models.DateTimeField(auto_now_add=True, verbose_name=_("Hochgeladen am"))

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = _("Bild")
        verbose_name_plural = _("Bilder")
        ordering = ["-date_uploaded"]
