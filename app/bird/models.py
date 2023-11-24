from datetime import date
from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from .choices import (
    CHOICE_AGE,
    CHOICE_CIRCUMSTANCES,
    CHOICE_FINDER,
    CHOICE_PLACE,
    CHOICE_SEX,
    CHOICE_STATUS,
)


def costs_default():
    return [{"date": date.today().strftime("%Y-%m-%d"), "cost_entry": "0.00"}]


class FallenBird(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    bird_identifier = models.CharField(
        max_length=256, verbose_name=_("Patienten Alias")
    )
    bird = models.ForeignKey(
        "Bird", default="1", on_delete=models.CASCADE, verbose_name=_("Vogel")
    )
    age = models.CharField(max_length=15, choices=CHOICE_AGE, verbose_name=_("Alter"))
    sex = models.CharField(
        max_length=15,
        choices=CHOICE_SEX,
        default="Unbekannt",
        verbose_name=_("Geschlecht"),
    )
    date_found = models.DateField(verbose_name=_("Datum des Fundes"))
    place_found = models.CharField(
        choices=CHOICE_PLACE,
        default="Innenstadt",
        verbose_name=_("Ort des Fundes"),
    )
    finder = models.TextField(
        choices=CHOICE_FINDER, default="Privatperson", verbose_name=_("Finder")
    )
    find_circumstances = models.CharField(
        choices=CHOICE_CIRCUMSTANCES, verbose_name=_("Fundumstände")
    )
    diagnosis_finding = models.TextField(
        null=True, blank=True, verbose_name=_("Diagnose bei Fund")
    )
    diagnosis_doctor = models.TextField(
        verbose_name=_("Diagnose durch Tierarzt"),
        null=True,
        blank=True,
    )
    comment = models.TextField(blank=True, null=True, verbose_name=_("Bemerkung"))
    status = models.CharField(choices=CHOICE_STATUS, null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Benutzer")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("angelegt am"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("geändert am"))

    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patienten")

    def __str__(self):
        return self.bird_identifier


class Bird(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256, unique=True, verbose_name=_("Bezeichnung"))
    description = RichTextField(null=True, blank=True, verbose_name=_("Erläuterungen"))

    class Meta:
        verbose_name = _("Vogel")
        verbose_name_plural = _("Vögel")
        ordering = ["name"]

    def __str__(self):
        return self.name
